"""
Authentication tools for Altiplano API.
"""

try:
    from ..server_factory import get_mcp_instance
    from ..config import BASE_URL, ALTIPLANO_USERNAME, ALTIPLANO_PASSWORD
    from ..utils import make_request
    from ..token_cache import get_cached_token, cache_token, clear_token_cache, get_token_info
except ImportError:
    from server_factory import get_mcp_instance
    from config import BASE_URL, ALTIPLANO_USERNAME, ALTIPLANO_PASSWORD
    from utils import make_request
    from token_cache import get_cached_token, cache_token, clear_token_cache, get_token_info

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def get_access_token(username: str = None, password: str = None) -> dict:
    """
    Get access token and refresh token by login method.
    Uses cached token if available and valid.
    
    Args:
        username: Username for authentication (default: from config)
        password: Password for authentication (default: from config)
        
    Returns:
        Dictionary containing access token and refresh token
    """
    # Use default credentials if not provided
    if username is None:
        username = ALTIPLANO_USERNAME
    if password is None:
        password = ALTIPLANO_PASSWORD
    
    # Check if we have a valid cached token
    cached_token = get_cached_token()
    if cached_token:
        token_info = get_token_info()
        return {
            "access_token": cached_token,
            "message": "Using cached token",
            "cached": True,
            "expires_at": token_info.get('expires_at'),
            "time_until_expiry": token_info.get('time_until_expiry')
        }
    
    # If no cached token, authenticate with server
    url = f"{BASE_URL}/rest/auth/login"
    auth = (username, password)
    
    # For login endpoint, send NO headers (server expects completely empty request)
    result = make_request("POST", url, auth=auth, headers={})
    
    # If authentication successful, cache the token
    if "access_token" in result:
        # Cache the token with expiration time from response
        expires_in = result.get("expiresIn", 3600)
        cache_token(result["access_token"], expires_in)
        result["cached"] = False
        result["message"] = "New token obtained and cached"
    
    return result


@mcp.tool()
def get_cached_token_info() -> dict:
    """
    Get information about the cached token.
    
    Returns:
        Dictionary with token cache information
    """
    return get_token_info()


@mcp.tool()
def clear_cached_token() -> dict:
    """
    Clear the cached authentication token.
    
    Returns:
        Dictionary with operation status
    """
    clear_token_cache()
    return {"status": "success", "message": "Token cache cleared"}


@mcp.tool()
def authenticate_with_cached_token() -> dict:
    """
    Get access token using cached credentials or prompt for new ones.
    This is a convenience function that automatically handles authentication.
    
    Returns:
        Dictionary containing access token information
    """
    # First try to get cached token
    cached_token = get_cached_token()
    if cached_token:
        token_info = get_token_info()
        return {
            "access_token": cached_token,
            "message": "Using cached token",
            "cached": True,
            "expires_at": token_info.get('expires_at'),
            "time_until_expiry": token_info.get('time_until_expiry')
        }
    
    # If no cached token, get a new one using default credentials
    return get_access_token() 