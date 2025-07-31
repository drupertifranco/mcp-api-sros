"""
Delete operations tools for Altiplano API.
"""

from ..server_factory import get_mcp_instance
from ..config import BASE_URL, DEFAULT_TARGETS
from ..utils import make_request, build_auth_headers

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def delete_internet(access_token: str, target: str = None) -> dict:
    """
    Delete Internet intent from network and controller.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: HSI#MED-03)
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["internet"]
        
    url = f"{BASE_URL}/rest/restconf/operations/ibn:delete-intent-from-network-and-controller"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:delete-intent-from-network-and-controller": {
            "intent-type": "l2-user",
            "target": target
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def delete_ont(access_token: str, target: str = None) -> dict:
    """
    Delete ONT intent from network and controller.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: MED-03)
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["ont"]
        
    url = f"{BASE_URL}/rest/restconf/operations/ibn:delete-intent-from-network-and-controller"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:delete-intent-from-network-and-controller": {
            "intent-type": "ont",
            "target": target
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def delete_infrastructure(access_token: str, target: str = None) -> dict:
    """
    Delete L2 infrastructure intent from network and controller.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: OLT1#HSI)
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["infrastructure"]
        
    url = f"{BASE_URL}/rest/restconf/operations/ibn:delete-intent-from-network-and-controller"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:delete-intent-from-network-and-controller": {
            "intent-type": "l2-infra",
            "target": target
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload) 