import http.server
import socketserver
import urllib.request
import urllib.parse
import json
import urllib.error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PORT = 8001
NVIDIA_API_KEY = os.getenv('NVIDIA_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

class ProxyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Accept')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # OpenWeatherMap proxies
        if parsed_path.path.startswith('/api/weather'):
            # Convert /api/weather/... to corresponding OpenWeather APIs
            query = parsed_path.query

            try:
                if parsed_path.path == '/api/weather/weather':
                    url = f'https://api.openweathermap.org/data/2.5/weather?{query}&appid={OPENWEATHER_API_KEY}'
                elif parsed_path.path == '/api/weather/forecast':
                    url = f'https://api.openweathermap.org/data/2.5/forecast?{query}&appid={OPENWEATHER_API_KEY}'
                elif parsed_path.path == '/api/weather/geo/direct':
                    url = f'https://api.openweathermap.org/geo/1.0/direct?{query}&appid={OPENWEATHER_API_KEY}'
                elif parsed_path.path == '/api/weather/uvi':
                    url = f'https://api.openweathermap.org/data/2.5/uvi?{query}&appid={OPENWEATHER_API_KEY}'
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"Not Found")
                    return

                req = urllib.request.Request(url)
                with urllib.request.urlopen(req) as response:
                    res_body = response.read()
                    self.send_response(response.getcode())
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(res_body)

            except urllib.error.HTTPError as e:
                self.send_response(e.code)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(e.read())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Use NVIDIA_API_KEY from environment instead of request headers
            req = urllib.request.Request(
                'https://integrate.api.nvidia.com/v1/chat/completions', 
                data=post_data, 
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {NVIDIA_API_KEY}',
                    'Accept': 'application/json'
                }
            )
            
            try:
                with urllib.request.urlopen(req) as response:
                    res_body = response.read()
                    self.send_response(response.getcode())
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(res_body)
            except urllib.error.HTTPError as e:
                self.send_response(e.code)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(e.read())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            super().do_POST()

with socketserver.TCPServer(("", PORT), ProxyRequestHandler) as httpd:
    print(f"Proxy and static file server running at http://localhost:{PORT}")
    httpd.serve_forever()
