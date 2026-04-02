import http.server
import socketserver
import urllib.request
import json
import urllib.error

PORT = 8001

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Accept')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Forward the request to NVIDIA
            req = urllib.request.Request(
                'https://integrate.api.nvidia.com/v1/chat/completions', 
                data=post_data, 
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': self.headers.get('Authorization', ''),
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

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Proxy and static file server running at http://localhost:{PORT}")
    httpd.serve_forever()
