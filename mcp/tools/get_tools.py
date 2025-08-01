"""
Get operations tools for Altiplano API.
"""

try:
    from ..server_factory import get_mcp_instance
    from ..config import BASE_URL, DEFAULT_TARGETS
    from ..utils import make_request, build_auth_headers
    from ..token_cache import get_cached_token
except ImportError:
    from server_factory import get_mcp_instance
    from config import BASE_URL, DEFAULT_TARGETS
    from utils import make_request, build_auth_headers
    from token_cache import get_cached_token

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def get_l2_user(access_token: str = None, intent_target: str = None) -> dict:
    """
    Get L2-User information.
    Automatically uses cached token if no access_token is provided.
    
    Args:
        access_token: Bearer token for authentication (optional, uses cached token if not provided)
        intent_target: Intent target identifier (default: HSI#MED-03)
        
    Returns:
        Dictionary with L2-User information
    """
    if intent_target is None:
        intent_target = DEFAULT_TARGETS["l2_user"]
    
    # Use cached token if no access_token provided
    if access_token is None:
        access_token = get_cached_token()
        if not access_token:
            return {
                "error": "No access token provided and no cached token available. Please authenticate first using get_access_token() or authenticate_with_cached_token()."
            }
    
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn/intent={intent_target},l2-user"
    headers = build_auth_headers(access_token)
    
    return make_request("GET", url, headers=headers) 