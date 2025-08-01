#!/usr/bin/env python3
"""
Test script to verify token caching functionality.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_cache_functionality():
    """Test the complete cache functionality."""
    print("🔐 Testing Token Cache Functionality")
    print("=" * 50)
    
    try:
        from tools.auth_tools import (
            get_access_token, get_cached_token_info, 
            clear_cached_token, authenticate_with_cached_token
        )
        from tools.get_tools import get_l2_user
        
        # Step 1: Clear any existing cache
        print("1. Clearing existing cache...")
        clear_cached_token()
        info = get_cached_token_info()
        print(f"   Cache info: {info}")
        
        # Step 2: Get a new token (should cache it)
        print("\n2. Getting new token...")
        result = get_access_token()
        print(f"   Result: {result.get('message', 'No message')}")
        print(f"   Cached: {result.get('cached', 'Unknown')}")
        
        # Step 3: Check cache status
        print("\n3. Checking cache status...")
        info = get_cached_token_info()
        print(f"   Cache info: {info}")
        
        # Step 4: Try to get token again (should use cached)
        print("\n4. Getting token again (should use cached)...")
        result2 = get_access_token()
        print(f"   Result: {result2.get('message', 'No message')}")
        print(f"   Cached: {result2.get('cached', 'Unknown')}")
        
        # Step 5: Test auto-authentication
        print("\n5. Testing auto-authentication...")
        result3 = authenticate_with_cached_token()
        print(f"   Result: {result3.get('message', 'No message')}")
        print(f"   Cached: {result3.get('cached', 'Unknown')}")
        
        # Step 6: Test using cached token in tools
        print("\n6. Testing cached token in tools...")
        try:
            l2_result = get_l2_user()  # Should use cached token
            print(f"   L2-User result: {l2_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Step 7: Check final cache status
        print("\n7. Final cache status...")
        info = get_cached_token_info()
        print(f"   Cache info: {info}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_cache_functionality()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Cache test completed!")
    else:
        print("❌ Cache test failed!")
        sys.exit(1) 