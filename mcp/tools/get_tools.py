"""
Get operations tools for Altiplano API.
"""

from ..server_factory import get_mcp_instance
from ..config import BASE_URL, DEFAULT_TARGETS
from ..utils import make_request, build_auth_headers

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def get_l2_user(access_token: str, intent_target: str = None) -> dict:
    """
    Get L2-User information.
    
    Args:
        access_token: Bearer token for authentication
        intent_target: Intent target identifier (default: HSI#MED-03)
        
    Returns:
        Dictionary with L2-User information
    """
    if intent_target is None:
        intent_target = DEFAULT_TARGETS["l2_user"]
        
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn/intent={intent_target},l2-user"
    headers = build_auth_headers(access_token)
    
    return make_request("GET", url, headers=headers) 