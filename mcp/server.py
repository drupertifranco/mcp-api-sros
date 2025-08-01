"""
Modular FastMCP server for Altiplano API endpoints.
Based on test-altiplano.postman_collection.json

This server uses a modular architecture with separate modules for different tool categories:
- Authentication tools
- Delete operations
- Create operations (ONT and L2-User)
- Get operations
- Infrastructure operations
- Sync operations
- Legacy tools (existing FastAPI endpoints)

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
from .server_factory import set_mcp_instance

# Create the MCP server instance
mcp = FastMCP(
    "Altiplano API Tools",    # Server name 
    "1.0.0"  # Server version
)

# Set the global instance for use in tool modules
set_mcp_instance(mcp)

# Import all tools from the modular structure
# This will register all the @mcp.tool() decorated functions
from .tools.auth_tools import get_access_token
from .tools.delete_tools import delete_internet, delete_ont, delete_infrastructure
from .tools.create_tools import (
    add_ont_bridge, add_ont_transparent,
    add_l2_user_hsi, add_l2_user_untagged, add_l2_user_transparent
)
from .tools.get_tools import get_l2_user
from .tools.infrastructure_tools import (
    create_residential_bridge_transparent, create_cross_connect, create_s_vlan_cross_connect
)
from .tools.sync_tools import sync_device_config
from .tools.legacy_tools import add_ip, delete_ip, get_public_ip

# Start the MCP server
if __name__ == "__main__":
    mcp.run()