#!/usr/bin/env python3
"""
Detailed authentication test script to try different approaches.
"""

import sys
import os
import requests

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_auth_no_headers():
    """Test authentication with no headers at all."""
    print("🔐 Test 1: No headers")
    print("=" * 30)
    
    try:
        url = "http://192.168.9.65/nokia-altiplano-ac/rest/auth/login"
        auth = ("adminuser", "password")
        
        response = requests.post(url, auth=auth, verify=False, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ SUCCESS!")
            return True
        else:
            print("❌ Failed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_auth_accept_only():
    """Test authentication with only Accept header."""
    print("\n🔐 Test 2: Accept header only")
    print("=" * 30)
    
    try:
        url = "http://192.168.9.65/nokia-altiplano-ac/rest/auth/login"
        auth = ("adminuser", "password")
        headers = {"Accept": "application/yang-data+json"}
        
        response = requests.post(url, auth=auth, headers=headers, verify=False, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ SUCCESS!")
            return True
        else:
            print("❌ Failed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_auth_content_type_json():
    """Test authentication with Content-Type: application/json."""
    print("\n🔐 Test 3: Content-Type application/json")
    print("=" * 30)
    
    try:
        url = "http://192.168.9.65/nokia-altiplano-ac/rest/auth/login"
        auth = ("adminuser", "password")
        headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, auth=auth, headers=headers, verify=False, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ SUCCESS!")
            return True
        else:
            print("❌ Failed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_auth_with_body():
    """Test authentication with empty JSON body."""
    print("\n🔐 Test 4: With empty JSON body")
    print("=" * 30)
    
    try:
        url = "http://192.168.9.65/nokia-altiplano-ac/rest/auth/login"
        auth = ("adminuser", "password")
        headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/json"
        }
        json_data = {}
        
        response = requests.post(url, auth=auth, headers=headers, json=json_data, verify=False, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ SUCCESS!")
            return True
        else:
            print("❌ Failed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_different_credentials():
    """Test with different credentials."""
    print("\n🔐 Test 5: Different credentials")
    print("=" * 30)
    
    credentials_to_try = [
        ("admin", "admin"),
        ("adminuser", "password"),
        ("admin", "password"),
        ("user", "password"),
        ("root", "root")
    ]
    
    for username, password in credentials_to_try:
        print(f"Trying: {username}/{password}")
        
        try:
            url = "http://192.168.9.65/nokia-altiplano-ac/rest/auth/login"
            auth = (username, password)
            
            response = requests.post(url, auth=auth, verify=False, timeout=10)
            print(f"  Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"  ✅ SUCCESS with {username}/{password}!")
                print(f"  Response: {response.text[:200]}...")
                return True
            elif response.status_code == 401:
                print(f"  ❌ Unauthorized")
            else:
                print(f"  ❌ Failed: {response.text[:100]}...")
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    return False

def test_different_endpoints():
    """Test different authentication endpoints."""
    print("\n🔐 Test 6: Different endpoints")
    print("=" * 30)
    
    endpoints_to_try = [
        "http://192.168.9.65/nokia-altiplano-ac/rest/auth/login",
        "http://192.168.9.65/altiplano-ac/rest/auth/login",
        "http://192.168.9.65/rest/auth/login",
        "http://192.168.9.65/nokia-altiplano-ac/auth/login",
        "http://192.168.9.65/nokia-altiplano-ac/api/auth/login"
    ]
    
    for endpoint in endpoints_to_try:
        print(f"Trying: {endpoint}")
        
        try:
            auth = ("adminuser", "password")
            
            response = requests.post(endpoint, auth=auth, verify=False, timeout=10)
            print(f"  Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"  ✅ SUCCESS with {endpoint}!")
                print(f"  Response: {response.text[:200]}...")
                return True
            elif response.status_code == 404:
                print(f"  ❌ Not Found")
            else:
                print(f"  ❌ Failed: {response.text[:100]}...")
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    return False

if __name__ == "__main__":
    print("🔍 Detailed Authentication Tests")
    print("=" * 50)
    
    tests = [
        test_auth_no_headers,
        test_auth_accept_only,
        test_auth_content_type_json,
        test_auth_with_body,
        test_different_credentials,
        test_different_endpoints
    ]
    
    success_count = 0
    for test in tests:
        if test():
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"📋 Results: {success_count}/{len(tests)} tests passed")
    
    if success_count > 0:
        print("🎉 Authentication working!")
    else:
        print("❌ All authentication tests failed")
        print("\n💡 Next steps:")
        print("  1. Check server documentation")
        print("  2. Verify credentials with server admin")
        print("  3. Check if server requires different authentication method")
        print("  4. Try connecting via Postman first") 