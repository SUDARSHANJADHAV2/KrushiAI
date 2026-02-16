#!/usr/bin/env python3
"""
Test script for KrushiAI Streamlit app
This script validates that the app can start and load correctly
"""

import subprocess
import sys
import time
import requests
import threading
import os

def test_streamlit_import():
    """Test if we can import the main app without errors"""
    try:
        print("Testing app import...")
        import main  # This will test all imports
        print("✓ App imports successfully")
        return True
    except Exception as e:
        print(f"✗ Import failed: {str(e)}")
        return False

def start_streamlit_server():
    """Start a Streamlit server in the background"""
    try:
        print("Starting Streamlit server...")
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", "8502",
            "--server.headless", "true"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        return process
    except Exception as e:
        print(f"Failed to start Streamlit server: {str(e)}")
        return None

def test_server_health(max_attempts=30):
    """Test if the Streamlit server is responding"""
    url = "http://localhost:8502/healthz"
    
    for attempt in range(max_attempts):
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print("✓ Streamlit server is healthy")
                return True
        except requests.exceptions.RequestException:
            pass
        
        print(f"Attempt {attempt + 1}/{max_attempts}: Waiting for server...")
        time.sleep(2)
    
    print("✗ Server health check failed")
    return False

def main():
    """Run all tests"""
    print("KrushiAI Streamlit Test Suite")
    print("=" * 50)
    
    # Change to the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Working directory: {os.getcwd()}")
    
    # Test 1: Import test
    if not test_streamlit_import():
        print("\n❌ Import test failed. Fix import issues before proceeding.")
        return False
    
    # Test 2: Server start test
    process = start_streamlit_server()
    if not process:
        print("\n❌ Failed to start Streamlit server")
        return False
    
    try:
        # Test 3: Health check
        if test_server_health():
            print("✅ All tests passed! App is ready for deployment.")
            result = True
        else:
            print("❌ Health check failed")
            result = False
            
    finally:
        # Clean up
        print("Shutting down test server...")
        process.terminate()
        process.wait()
    
    return result

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)