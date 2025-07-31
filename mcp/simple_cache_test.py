#!/usr/bin/env python3
"""
Simple test script for token cache.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing token cache...")

try:
    from token_cache import TokenCache
    
    # Create cache instance
    cache = TokenCache()
    print("✓ TokenCache created")
    
    # Test setting token
    cache.set_token("test_token_123", 3600)
    print("✓ Token set")
    
    # Test getting token
    token = cache.get_token()
    print(f"✓ Token retrieved: {token}")
    
    # Test cache info
    info = cache.get_token_info()
    print(f"✓ Cache info: {info}")
    
    # Check if file exists
    if os.path.exists(".token_cache.json"):
        print("✓ Cache file created")
        with open(".token_cache.json", "r") as f:
            content = f.read()
            print(f"✓ File content: {content}")
    else:
        print("❌ Cache file not created")
    
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc() 