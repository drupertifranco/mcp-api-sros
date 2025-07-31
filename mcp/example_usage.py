#!/usr/bin/env python3
"""
Example usage of the MCP server with authentication and token caching.
This script demonstrates how to use the tools with automatic authentication.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def example_authentication():
    """Example of authentication workflow."""
    print("🔐 Authentication Example")
    print("=" * 40)
    
    try:
        from tools.auth_tools import (
            get_access_token, get_cached_token_info, 
            clear_cached_token, authenticate_with_cached_token
        )
        
        # Clear any existing cache
        clear_cached_token()
        print("✓ Cache cleared")
        
        # Check initial cache status
        info = get_cached_token_info()
        print(f"✓ Initial cache info: {info}")
        
        # Example 1: Get token with default credentials
        print("\n1. Getting token with default credentials...")
        result = get_access_token()  # Uses config defaults
        print(f"   Result: {result}")
        
        # Example 2: Check cache status after authentication
        print("\n2. Checking cache status...")
        info = get_cached_token_info()
        print(f"   Cache info: {info}")
        
        # Example 3: Use automatic authentication
        print("\n3. Using automatic authentication...")
        result = authenticate_with_cached_token()
        print(f"   Result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def example_auto_auth_tools():
    """Example of using tools with automatic authentication."""
    print("\n🛠️ Auto-Authentication Tools Example")
    print("=" * 40)
    
    try:
        from tools.get_tools import get_l2_user
        from tools.delete_tools import delete_internet
        from tools.auth_tools import get_cached_token_info
        
        # Check if we have a cached token
        info = get_cached_token_info()
        if not info.get('is_valid', False):
            print("⚠️  No valid cached token. Some operations may fail.")
            print("   Run get_access_token() first to authenticate.")
        
        # Example 1: Get L2-User info (will use cached token if available)
        print("\n1. Getting L2-User information...")
        result = get_l2_user()  # No access_token needed!
        print(f"   Result: {result}")
        
        # Example 2: Delete operation (will use cached token if available)
        print("\n2. Attempting delete operation...")
        result = delete_internet()  # No access_token needed!
        print(f"   Result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def example_manual_auth():
    """Example of manual authentication workflow."""
    print("\n👤 Manual Authentication Example")
    print("=" * 40)
    
    try:
        from tools.auth_tools import get_access_token
        from tools.get_tools import get_l2_user
        
        # Example: Manual authentication with specific credentials
        print("1. Manual authentication with specific credentials...")
        result = get_access_token("admin", "admin")  # Replace with real credentials
        print(f"   Result: {result}")
        
        if "access_token" in result:
            # Use the token manually
            print("\n2. Using token manually...")
            user_result = get_l2_user(access_token=result["access_token"])
            print(f"   Result: {user_result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def example_cache_management():
    """Example of cache management."""
    print("\n🗂️ Cache Management Example")
    print("=" * 40)
    
    try:
        from tools.auth_tools import (
            get_cached_token_info, clear_cached_token
        )
        
        # Check current cache status
        print("1. Current cache status:")
        info = get_cached_token_info()
        print(f"   {info}")
        
        # Clear cache
        print("\n2. Clearing cache...")
        result = clear_cached_token()
        print(f"   Result: {result}")
        
        # Check cache after clearing
        print("\n3. Cache status after clearing:")
        info = get_cached_token_info()
        print(f"   {info}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 MCP Server Authentication Examples")
    print("=" * 50)
    
    success1 = example_authentication()
    success2 = example_auto_auth_tools()
    success3 = example_manual_auth()
    success4 = example_cache_management()
    
    print("\n" + "=" * 50)
    if all([success1, success2, success3, success4]):
        print("✅ All examples completed successfully!")
        print("\nKey Features Demonstrated:")
        print("  ✓ Automatic token caching")
        print("  ✓ Tools with auto-authentication")
        print("  ✓ Manual authentication")
        print("  ✓ Cache management")
        print("\nNext Steps:")
        print("  1. Configure your credentials in config.py")
        print("  2. Run: python standalone_server.py")
        print("  3. Use the tools with automatic authentication!")
    else:
        print("❌ Some examples failed.")
        sys.exit(1) 