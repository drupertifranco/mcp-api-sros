"""
Create operations tools for Altiplano API (ONT and L2-User).
"""

try:
    from ..server_factory import get_mcp_instance
    from ..config import (
        BASE_URL, DEFAULT_TARGETS, DEFAULT_SERIAL_NUMBER, DEFAULT_FIBER_NAME,
        INTENT_VERSIONS, SERVICE_PROFILES
    )
    from ..utils import make_request, build_auth_headers, require_auth_token
except ImportError:
    from server_factory import get_mcp_instance
    from config import (
        BASE_URL, DEFAULT_TARGETS, DEFAULT_SERIAL_NUMBER, DEFAULT_FIBER_NAME,
        INTENT_VERSIONS, SERVICE_PROFILES
    )
    from utils import make_request, build_auth_headers, require_auth_token

# Get the MCP instance
mcp = get_mcp_instance()


# ONT Creation Tools
@mcp.tool()
def add_ont_bridge(
    access_token: str = None, 
    target: str = None, 
    serial_number: str = None, 
    fiber_name: str = None
) -> dict:
    """
    Add ONT with bridge type.
    Automatically uses cached token if no access_token is provided.
    
    Args:
        access_token: Bearer token for authentication (optional, uses cached token if not provided)
        target: Target identifier (default: MED-03)
        serial_number: ONT serial number (default: ALCLFCA06F4B)
        fiber_name: Fiber name (default: PON1_OLT1)
        
    Returns:
        Dictionary with operation status
    """
    # Check authentication
    auth_result = require_auth_token(access_token)
    if "error" in auth_result:
        return auth_result
    access_token = auth_result["access_token"]
    
    if target is None:
        target = DEFAULT_TARGETS["ont"]
    if serial_number is None:
        serial_number = DEFAULT_SERIAL_NUMBER
    if fiber_name is None:
        fiber_name = DEFAULT_FIBER_NAME
        
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "ont",
            "intent-specific-data": {
                "ont:ont": {
                    "ont-type": "bridge",
                    "from-device-mapping": [None],
                    "onu-service-profile": "default-by-l2-user",
                    "pon-type": "gpon",
                    "expected-serial-number": serial_number,
                    "uni-service-configuration": [
                        {
                            "service-profile": "default-by-l2-user",
                            "uni-id": "LAN1"
                        }
                    ],
                    "fiber-name": fiber_name
                }
            },
            "intent-type-version": INTENT_VERSIONS["ont"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def add_ont_transparent(
    access_token: str, 
    target: str = None, 
    serial_number: str = None, 
    fiber_name: str = None
) -> dict:
    """
    Add ONT with transparent type.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: MED-03)
        serial_number: ONT serial number (default: ALCLFCA06F4B)
        fiber_name: Fiber name (default: PON1_OLT1)
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["ont"]
    if serial_number is None:
        serial_number = DEFAULT_SERIAL_NUMBER
    if fiber_name is None:
        fiber_name = DEFAULT_FIBER_NAME
        
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "ont",
            "intent-specific-data": {
                "ont:ont": {
                    "ont-type": "transparente",
                    "from-device-mapping": [None],
                    "onu-service-profile": "default-by-l2-user",
                    "pon-type": "gpon",
                    "expected-serial-number": serial_number,
                    "uni-service-configuration": [
                        {
                            "service-profile": "default-by-l2-user",
                            "uni-id": "LAN1"
                        }
                    ],
                    "fiber-name": fiber_name
                }
            },
            "intent-type-version": INTENT_VERSIONS["ont"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


# L2-User Creation Tools
@mcp.tool()
def add_l2_user_hsi(
    access_token: str, 
    target: str = "HSI-11#MED-03", 
    user_device_name: str = "MED-03", 
    customer_id: str = "MED-03", 
    q_vlan_id: int = 11
) -> dict:
    """
    Add L2-User with HSI configuration.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier
        user_device_name: User device name
        customer_id: Customer identifier
        q_vlan_id: Q-VLAN ID
        
    Returns:
        Dictionary with operation status
    """
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "l2-user",
            "intent-specific-data": {
                "l2-user:l2-user": {
                    "l2-infra": "HSI",
                    "service-profile": SERVICE_PROFILES["internet"],
                    "speed-profile": SERVICE_PROFILES["speed"],
                    "user-device-name": user_device_name,
                    "customer-id": customer_id,
                    "q-vlan-id": q_vlan_id,
                    "uni-id": "LAN1"
                }
            },
            "intent-type-version": INTENT_VERSIONS["l2_user"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def add_l2_user_untagged(
    access_token: str, 
    target: str = "HSI-11#MED-01", 
    user_device_name: str = "MED-01", 
    customer_id: str = "MED-01"
) -> dict:
    """
    Add L2-User with untagged configuration.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier
        user_device_name: User device name
        customer_id: Customer identifier
        
    Returns:
        Dictionary with operation status
    """
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "l2-user",
            "intent-specific-data": {
                "l2-user:l2-user": {
                    "l2-infra": "HSI",
                    "service-profile": SERVICE_PROFILES["internet"],
                    "speed-profile": SERVICE_PROFILES["speed"],
                    "user-device-name": user_device_name,
                    "customer-id": customer_id,
                    "uni-id": "LAN1",
                    "untagged": [None]
                }
            },
            "intent-type-version": INTENT_VERSIONS["l2_user"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def add_l2_user_transparent(
    access_token: str, 
    target: str = "HSI#MED-03", 
    user_device_name: str = "MED-01", 
    customer_id: str = "MED-01", 
    transparent_q_vlan_id: int = 15
) -> dict:
    """
    Add L2-User with transparent configuration.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier
        user_device_name: User device name
        customer_id: Customer identifier
        transparent_q_vlan_id: Transparent Q-VLAN ID
        
    Returns:
        Dictionary with operation status
    """
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "l2-user",
            "intent-specific-data": {
                "l2-user:l2-user": {
                    "l2-infra": "HSI",
                    "service-profile": SERVICE_PROFILES["internet"],
                    "speed-profile": SERVICE_PROFILES["speed"],
                    "user-device-name": user_device_name,
                    "customer-id": customer_id,
                    "uni-id": "LAN1",
                    "transparent-q-vlan-id": transparent_q_vlan_id
                }
            },
            "intent-type-version": INTENT_VERSIONS["l2_user"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload) 