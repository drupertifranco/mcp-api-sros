#!/usr/bin/env python3
"""
Test script to verify authentication and token caching functionality.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_config():
    """Test configuration loading."""
    print("Testing configuration...")
    
    try:
        from config import (
            BASE_URL, ALTIPLANO_USERNAME, ALTIPLANO_PASSWORD, 
            TOKEN_CACHE_DURATION, TOKEN_CACHE_FILE
        )
        
        print(f"✓ BASE_URL: {BASE_URL}")
        print(f"✓ Username: {ALTIPLANO_USERNAME}")
        print(f"✓ Password: {'*' * len(ALTIPLANO_PASSWORD)}")
        print(f"✓ Cache duration: {TOKEN_CACHE_DURATION} seconds")
        print(f"✓ Cache file: {TOKEN_CACHE_FILE}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return False

def test_token_cache():
    """Test token cache functionality."""
    print("\nTesting token cache...")
    
    try:
        from token_cache import (
            get_cached_token, cache_token, clear_token_cache, 
            is_token_cached, get_token_info
        )
        
        # Test initial state
        print("✓ Token cache functions imported")
        
        # Test cache info
        info = get_token_info()
        print(f"✓ Cache info: {info}")
        
        # Test caching a token
        test_token = "test_token_12345"
        cache_token(test_token, 3600)
        print("✓ Test token cached")
        
        # Test retrieving cached token
        cached = get_cached_token()
        if cached == test_token:
            print("✓ Cached token retrieved correctly")
        else:
            print(f"❌ Token mismatch: expected {test_token}, got {cached}")
            return False
        
        # Test cache status
        if is_token_cached():
            print("✓ Token cache status: valid")
        else:
            print("❌ Token cache status: invalid")
            return False
        
        # Test cache info after caching
        info = get_token_info()
        print(f"✓ Updated cache info: {info}")
        
        # Clear cache
        clear_token_cache()
        print("✓ Cache cleared")
        
        # Verify cache is cleared
        if not is_token_cached():
            print("✓ Cache cleared successfully")
        else:
            print("❌ Cache not cleared properly")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing token cache: {e}")
        return False

def test_auth_tools():
    """Test authentication tools."""
    print("\nTesting authentication tools...")
    
    try:
        from tools.auth_tools import (
            get_access_token, get_cached_token_info, 
            clear_cached_token, authenticate_with_cached_token
        )
        
        print("✓ Authentication tools imported")
        
        # Test get_cached_token_info
        info = get_cached_token_info()
        print(f"✓ Token info: {info}")
        
        # Test clear_cached_token
        result = clear_cached_token()
        print(f"✓ Clear cache result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing auth tools: {e}")
        return False

def test_auto_auth():
    """Test automatic authentication in tools."""
    print("\nTesting automatic authentication...")
    
    try:
        from tools.get_tools import get_l2_user
        from tools.delete_tools import delete_internet
        
        print("✓ Tools with auto-auth imported")
        
        # Test get_l2_user without token (should return error)
        result = get_l2_user()
        if "error" in result:
            print("✓ get_l2_user correctly requires authentication")
        else:
            print("❌ get_l2_user should require authentication")
            return False
        
        # Test delete_internet without token (should return error)
        result = delete_internet()
        if "error" in result:
            print("✓ delete_internet correctly requires authentication")
        else:
            print("❌ delete_internet should require authentication")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing auto-auth: {e}")
        return False

if __name__ == "__main__":
    print("🔐 Testing Authentication & Token Cache")
    print("=" * 50)
    
    success1 = test_config()
    success2 = test_token_cache()
    success3 = test_auth_tools()
    success4 = test_auto_auth()
    
    print("\n" + "=" * 50)
    if all([success1, success2, success3, success4]):
        print("✅ All authentication tests passed!")
        print("\nAuthentication features:")
        print("  ✓ Configuration with default credentials")
        print("  ✓ Token caching with expiration")
        print("  ✓ Automatic token usage in tools")
        print("  ✓ Cache management functions")
        sys.exit(0)
    else:
        print("❌ Some authentication tests failed.")
        sys.exit(1) 