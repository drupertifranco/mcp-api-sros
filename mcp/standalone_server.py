#!/usr/bin/env python3
"""
Standalone MCP server for Altiplano API endpoints.
This version doesn't use relative imports and can be run directly.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP(
    "Altiplano API Tools",    # Server name 
    "1.0.0"  # Server version
)

# Import configuration and utilities
from config import BASE_URL, DEFAULT_HEADERS, FASTAPI_BASE_URL
from utils import make_request, build_auth_headers
from server_factory import set_mcp_instance

# Set the global instance
set_mcp_instance(mcp)

# Import all tool modules to register their tools
print("Loading MCP tools...")

# Auth tools
import tools.auth_tools
print("✓ Loaded auth tools")

# Delete tools  
import tools.delete_tools
print("✓ Loaded delete tools")

# Create tools
import tools.create_tools
print("✓ Loaded create tools")

# Get tools
import tools.get_tools
print("✓ Loaded get tools")

# Infrastructure tools
import tools.infrastructure_tools
print("✓ Loaded infrastructure tools")

# Sync tools
import tools.sync_tools
print("✓ Loaded sync tools")

# Legacy tools
import tools.legacy_tools
print("✓ Loaded legacy tools")

print("✅ All tools loaded successfully!")

# Start the MCP server
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run() 