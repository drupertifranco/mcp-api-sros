"""
Infrastructure tools for Altiplano API.
"""

from ..server_factory import get_mcp_instance
from ..config import (
    BASE_URL, DEFAULT_TARGETS, DEFAULT_NNI_ID, 
    INTENT_VERSIONS, SERVICE_PROFILES
)
from ..utils import make_request, build_auth_headers

# Get the MCP instance
mcp = get_mcp_instance()


@mcp.tool()
def create_residential_bridge_transparent(
    access_token: str, 
    target: str = None, 
    nni_id: str = None, 
    c_vlan_id: int = 15
) -> dict:
    """
    Create residential bridge transparent infrastructure.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: OLT1#HSI)
        nni_id: NNI identifier (default: nt-a:xfp:1)
        c_vlan_id: C-VLAN ID
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["infrastructure"]
    if nni_id is None:
        nni_id = DEFAULT_NNI_ID
        
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "l2-infra",
            "intent-specific-data": {
                "l2-infra:l2-infra": {
                    "nni-id": nni_id,
                    "none": [None],
                    "c-vlan-id": c_vlan_id,
                    "forwarder-profile": SERVICE_PROFILES["unicast"],
                    "service-profile": SERVICE_PROFILES["unicast_l2cp"],
                    "vlan-mode": "residential-bridge"
                }
            },
            "intent-type-version": INTENT_VERSIONS["l2_infra"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def create_cross_connect(
    access_token: str, 
    target: str = None, 
    nni_id: str = None, 
    s_vlan_id: int = 15
) -> dict:
    """
    Create cross-connect infrastructure.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: OLT1#HSI)
        nni_id: NNI identifier (default: nt-a:xfp:1)
        s_vlan_id: S-VLAN ID
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["infrastructure"]
    if nni_id is None:
        nni_id = DEFAULT_NNI_ID
        
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "l2-infra",
            "intent-specific-data": {
                "l2-infra:l2-infra": {
                    "nni-id": nni_id,
                    "none": [None],
                    "s-vlan-id": s_vlan_id,
                    "forwarder-profile": SERVICE_PROFILES["unicast"],
                    "service-profile": SERVICE_PROFILES["unicast"],
                    "vlan-mode": "cross-connect"
                }
            },
            "intent-type-version": INTENT_VERSIONS["l2_infra"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload)


@mcp.tool()
def create_s_vlan_cross_connect(
    access_token: str, 
    target: str = None, 
    nni_id: str = None, 
    s_vlan_id: int = 15
) -> dict:
    """
    Create S-VLAN cross-connect infrastructure.
    
    Args:
        access_token: Bearer token for authentication
        target: Target identifier (default: OLT1#HSI)
        nni_id: NNI identifier (default: nt-a:xfp:1)
        s_vlan_id: S-VLAN ID
        
    Returns:
        Dictionary with operation status
    """
    if target is None:
        target = DEFAULT_TARGETS["infrastructure"]
    if nni_id is None:
        nni_id = DEFAULT_NNI_ID
        
    url = f"{BASE_URL}/rest/restconf/data/ibn:ibn?altiplano-triggerSyncUponSuccess=true"
    headers = build_auth_headers(access_token)
    
    payload = {
        "ibn:intent": {
            "target": target,
            "intent-type": "l2-infra",
            "intent-specific-data": {
                "l2-infra:l2-infra": {
                    "nni-id": nni_id,
                    "none": [None],
                    "s-vlan-id": s_vlan_id,
                    "forwarder-profile": SERVICE_PROFILES["unicast"],
                    "service-profile": SERVICE_PROFILES["unicast"],
                    "vlan-mode": "s-vlan-cross-connect"
                }
            },
            "intent-type-version": INTENT_VERSIONS["l2_infra"],
            "required-network-state": "active"
        }
    }
    
    return make_request("POST", url, headers=headers, json_data=payload) 