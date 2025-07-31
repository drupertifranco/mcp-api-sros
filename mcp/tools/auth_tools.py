"""
Authentication tools for Altiplano API.
"""

from ..server_factory import get_mcp_instance
from ..config import BASE_URL
from ..utils import make_request

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def get_access_token(username: str, password: str) -> dict:
    """
    Get access token and refresh token by login method.
    
    Args:
        username: Username for authentication
        password: Password for authentication
        
    Returns:
        Dictionary containing access token and refresh token
    """
    url = f"{BASE_URL}/rest/auth/login"
    auth = (username, password)
    
    return make_request("POST", url, auth=auth) 