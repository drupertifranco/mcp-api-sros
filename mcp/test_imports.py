#!/usr/bin/env python3
"""
Test script to verify all imports work correctly.
Run with: python test_imports.py
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all imports to ensure they work correctly."""
    print("Testing imports...")
    
    try:
        # Test core modules
        print("✓ Testing core modules...")
        from config import BASE_URL, DEFAULT_HEADERS
        from utils import make_request, build_auth_headers
        from server_factory import get_mcp_instance, set_mcp_instance
        
        # Test tool modules
        print("✓ Testing tool modules...")
        import tools.auth_tools
        import tools.delete_tools
        import tools.create_tools
        import tools.get_tools
        import tools.infrastructure_tools
        import tools.sync_tools
        import tools.legacy_tools
        
        # Test MCP server
        print("✓ Testing MCP server...")
        from mcp.server.fastmcp import FastMCP
        
        print("✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1) 