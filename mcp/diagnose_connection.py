#!/usr/bin/env python3
"""
Diagnostic script to test connectivity to Altiplano server.
"""

import sys
import os
import requests
from urllib.parse import urlparse

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_config():
    """Test configuration loading."""
    print("🔧 Configuration Test")
    print("=" * 40)
    
    try:
        from config import (
            BASE_URL, ALTIPLANO_USERNAME, ALTIPLANO_PASSWORD, 
            VERIFY_SSL, DEFAULT_HEADERS
        )
        
        print(f"✓ BASE_URL: {BASE_URL}")
        print(f"✓ Username: {ALTIPLANO_USERNAME}")
        print(f"✓ Password: {'*' * len(ALTIPLANO_PASSWORD)}")
        print(f"✓ VERIFY_SSL: {VERIFY_SSL}")
        print(f"✓ Headers: {DEFAULT_HEADERS}")
        
        # Parse URL to check protocol
        parsed = urlparse(BASE_URL)
        print(f"✓ Protocol: {parsed.scheme}")
        print(f"✓ Host: {parsed.hostname}")
        print(f"✓ Port: {parsed.port or 'default'}")
        print(f"✓ Path: {parsed.path}")
        
        return BASE_URL, ALTIPLANO_USERNAME, ALTIPLANO_PASSWORD
        
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return None, None, None

def test_basic_connectivity(base_url):
    """Test basic connectivity to the server."""
    print("\n🌐 Basic Connectivity Test")
    print("=" * 40)
    
    try:
        # Test HTTP connectivity
        print(f"Testing connection to: {base_url}")
        
        # Try a simple GET request to the base URL
        response = requests.get(base_url, verify=False, timeout=10)
        print(f"✓ HTTP Status: {response.status_code}")
        print(f"✓ Response headers: {dict(response.headers)}")
        
        return True
        
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Connection Error: {e}")
        return False
    except requests.exceptions.Timeout as e:
        print(f"❌ Timeout Error: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return False

def test_auth_endpoint(base_url, username, password):
    """Test authentication endpoint specifically."""
    print("\n🔐 Authentication Endpoint Test")
    print("=" * 40)
    
    try:
        auth_url = f"{base_url}/rest/auth/login"
        print(f"Testing auth endpoint: {auth_url}")
        
        # Test with basic auth
        auth = (username, password)
        headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"
        }
        
        print(f"Using credentials: {username}/{'*' * len(password)}")
        
        response = requests.post(
            auth_url, 
            auth=auth, 
            headers=headers, 
            verify=False, 
            timeout=10
        )
        
        print(f"✓ HTTP Status: {response.status_code}")
        print(f"✓ Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"✓ Response data: {data}")
                return True
            except:
                print(f"✓ Response text: {response.text[:200]}...")
                return True
        else:
            print(f"❌ Error response: {response.text[:200]}...")
            return False
            
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Connection Error: {e}")
        return False
    except requests.exceptions.Timeout as e:
        print(f"❌ Timeout Error: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return False

def test_alternative_urls():
    """Test alternative URL formats."""
    print("\n🔄 Alternative URL Test")
    print("=" * 40)
    
    base_host = "192.168.9.65"
    paths = [
        "/nokia-altiplano-ac",
        "/altiplano-ac", 
        "/",
        "/rest"
    ]
    
    for path in paths:
        for protocol in ["http", "https"]:
            for port in [None, 80, 443, 8080, 8443]:
                if port:
                    url = f"{protocol}://{base_host}:{port}{path}"
                else:
                    url = f"{protocol}://{base_host}{path}"
                
                print(f"Testing: {url}")
                
                try:
                    response = requests.get(url, verify=False, timeout=5)
                    print(f"  ✓ Status: {response.status_code}")
                    if response.status_code == 200:
                        print(f"  ✓ Success! This URL works: {url}")
                        return url
                except:
                    print(f"  ❌ Failed")
                    continue
    
    return None

def test_network_reachability():
    """Test basic network reachability."""
    print("\n📡 Network Reachability Test")
    print("=" * 40)
    
    import subprocess
    import platform
    
    host = "192.168.9.65"
    
    # Determine ping command based on OS
    if platform.system().lower() == "windows":
        ping_cmd = ["ping", "-n", "1", host]
    else:
        ping_cmd = ["ping", "-c", "1", host]
    
    try:
        result = subprocess.run(ping_cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✓ Host {host} is reachable")
            print(f"✓ Ping output: {result.stdout}")
            return True
        else:
            print(f"❌ Host {host} is not reachable")
            print(f"❌ Ping output: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"❌ Ping timeout for {host}")
        return False
    except Exception as e:
        print(f"❌ Ping error: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Altiplano Connection Diagnostic")
    print("=" * 50)
    
    # Test 1: Configuration
    base_url, username, password = test_config()
    if not base_url:
        sys.exit(1)
    
    # Test 2: Network reachability
    network_ok = test_network_reachability()
    
    # Test 3: Basic connectivity
    if network_ok:
        connectivity_ok = test_basic_connectivity(base_url)
    else:
        print("⚠️  Skipping connectivity test due to network issues")
        connectivity_ok = False
    
    # Test 4: Authentication endpoint
    if connectivity_ok:
        auth_ok = test_auth_endpoint(base_url, username, password)
    else:
        print("⚠️  Skipping auth test due to connectivity issues")
        auth_ok = False
    
    # Test 5: Alternative URLs
    if not connectivity_ok:
        print("\n🔍 Trying alternative URLs...")
        alternative_url = test_alternative_urls()
        if alternative_url:
            print(f"🎉 Found working URL: {alternative_url}")
            print("Update your config.py with this URL!")
    
    print("\n" + "=" * 50)
    print("📋 Summary:")
    print(f"  Network reachable: {'✓' if network_ok else '❌'}")
    print(f"  Basic connectivity: {'✓' if connectivity_ok else '❌'}")
    print(f"  Authentication: {'✓' if auth_ok else '❌'}")
    
    if not network_ok:
        print("\n💡 Suggestions:")
        print("  1. Check if the server is running")
        print("  2. Verify the IP address is correct")
        print("  3. Check firewall settings")
        print("  4. Try connecting from another machine")
    
    elif not connectivity_ok:
        print("\n💡 Suggestions:")
        print("  1. Check if the server is listening on the correct port")
        print("  2. Try different URL formats (see alternative URLs above)")
        print("  3. Check if the server requires HTTPS")
        print("  4. Verify the base path is correct")
    
    elif not auth_ok:
        print("\n💡 Suggestions:")
        print("  1. Verify username and password are correct")
        print("  2. Check if the authentication endpoint is correct")
        print("  3. Try different authentication methods")
        print("  4. Check server logs for authentication errors") 