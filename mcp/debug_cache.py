#!/usr/bin/env python3
"""
Debug script to troubleshoot token cache issues.
"""

import sys
import os
import json

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def debug_cache():
    """Debug the cache functionality step by step."""
    print("🔍 Debugging Token Cache")
    print("=" * 50)
    
    try:
        from token_cache import TokenCache, cache_token, get_cached_token, get_token_info
        
        # Test 1: Direct cache operations
        print("1. Testing direct cache operations...")
        
        # Create a test token
        test_token = "test_token_12345"
        print(f"   Test token: {test_token}")
        
        # Try to cache it
        print("   Caching token...")
        cache_token(test_token, 3600)
        
        # Check if it was cached
        print("   Retrieving cached token...")
        cached = get_cached_token()
        print(f"   Retrieved: {cached}")
        
        # Check cache info
        print("   Getting cache info...")
        info = get_token_info()
        print(f"   Info: {info}")
        
        # Test 2: Check if file was created
        print("\n2. Checking cache file...")
        cache_file = ".token_cache.json"
        if os.path.exists(cache_file):
            print(f"   ✓ Cache file exists: {cache_file}")
            with open(cache_file, 'r') as f:
                content = f.read()
                print(f"   Content: {content}")
        else:
            print(f"   ❌ Cache file does not exist: {cache_file}")
        
        # Test 3: Test TokenCache class directly
        print("\n3. Testing TokenCache class directly...")
        cache = TokenCache()
        
        # Clear any existing cache
        cache.clear_cache()
        print("   Cache cleared")
        
        # Set a token
        cache.set_token("direct_test_token", 3600)
        print("   Token set directly")
        
        # Get the token
        token = cache.get_token()
        print(f"   Retrieved: {token}")
        
        # Check info
        info = cache.get_token_info()
        print(f"   Info: {info}")
        
        # Test 4: Check file again
        print("\n4. Checking cache file after direct operations...")
        if os.path.exists(cache_file):
            print(f"   ✓ Cache file exists: {cache_file}")
            with open(cache_file, 'r') as f:
                content = f.read()
                print(f"   Content: {content}")
        else:
            print(f"   ❌ Cache file still does not exist: {cache_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = debug_cache()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Debug completed!")
    else:
        print("❌ Debug failed!")
        sys.exit(1) 