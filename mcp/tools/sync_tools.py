"""
Sync operations tools for Altiplano API.
"""

from ..server_factory import get_mcp_instance
from ..config import BASE_URL
from ..utils import make_request, build_auth_headers

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def sync_device_config(access_token: str, intent_target: str = "OLT1,device-config-fx") -> dict:
    """
    Synchronize device configuration.
    
    Args:
        access_token: Bearer token for authentication
        intent_target: Intent target identifier
        
    Returns:
        Dictionary with operation status
    """
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn/intent={intent_target}/synchronize"
    headers = build_auth_headers(access_token)
    
    return make_request("POST", url, headers=headers) 