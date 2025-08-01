#!/usr/bin/env python3
"""
Standalone MCP server runner for Altiplano API endpoints.
This file can be run directly with: uv run mcp dev run_server.py
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

# Import and register all tools
from server_factory import set_mcp_instance
set_mcp_instance(mcp)

# Import all tool modules to register their tools
import tools.auth_tools
import tools.delete_tools
import tools.create_tools
import tools.get_tools
import tools.infrastructure_tools
import tools.sync_tools
import tools.legacy_tools

# Start the MCP server
if __name__ == "__main__":
    mcp.run() 