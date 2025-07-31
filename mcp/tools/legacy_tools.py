"""
Legacy tools for existing FastAPI endpoints.
"""

try:
    from ..server_factory import get_mcp_instance
    from ..config import FASTAPI_BASE_URL
    from ..utils import make_request
except ImportError:
    from server_factory import get_mcp_instance
    from config import FASTAPI_BASE_URL
    from utils import make_request

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def add_ip(prefix_name: str, prefix: str) -> dict:
    """
    Add an IP prefix using the FastAPI application.
    
    Args:
        prefix_name: Name of the IP prefix
        prefix: IP prefix in CIDR notation
        
    Returns:
        Dictionary with operation status
    """
    url = f"{FASTAPI_BASE_URL}/add-ip"
    payload = {
        "prefix_name": prefix_name,
        "prefix": prefix
    }
    
    return make_request("POST", url, json_data=payload)


@mcp.tool()
def delete_ip(prefix_name: str, prefix: str) -> dict:
    """
    Delete an IP prefix using the FastAPI application.
    
    Args:
        prefix_name: Name of the IP prefix
        prefix: IP prefix in CIDR notation
        
    Returns:
        Dictionary with operation status
    """
    url = f"{FASTAPI_BASE_URL}/delete-ip"
    payload = {
        "prefix_name": prefix_name,
        "prefix": prefix
    }
    
    return make_request("DELETE", url, json_data=payload)


@mcp.tool()
def get_public_ip() -> dict:
    """
    Get the public IP address of the server.
    
    Returns:
        Dictionary with public IP information
    """
    url = "https://ifconfig.me/all.json"
    
    return make_request("GET", url) 