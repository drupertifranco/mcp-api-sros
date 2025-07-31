"""
Utility functions for the MCP server.
"""

import requests
from typing import Dict, Any, Optional
from .config import DEFAULT_HEADERS


def make_request(
    method: str,
    url: str,
    headers: Optional[Dict[str, str]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    auth: Optional[tuple] = None,
    verify_ssl: bool = False
) -> Dict[str, Any]:
    """
    Make HTTP requests with consistent error handling.
    
    Args:
        method: HTTP method (GET, POST, DELETE, etc.)
        url: Request URL
        headers: Request headers
        json_data: JSON payload for POST/PUT requests
        auth: Authentication tuple (username, password)
        verify_ssl: Whether to verify SSL certificates
        
    Returns:
        Dictionary with response data or error information
    """
    try:
        # Merge default headers with provided headers
        request_headers = {**DEFAULT_HEADERS}
        if headers:
            request_headers.update(headers)
        
        # Make the request
        response = requests.request(
            method=method,
            url=url,
            headers=request_headers,
            json=json_data,
            auth=auth,
            verify=verify_ssl
        )
        
        response.raise_for_status()
        
        # Return response data
        if response.content:
            return response.json()
        else:
            return {"status": "success", "status_code": response.status_code}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid JSON response: {str(e)}"}


def build_auth_headers(access_token: str) -> Dict[str, str]:
    """
    Build headers with authentication token.
    
    Args:
        access_token: Bearer token for authentication
        
    Returns:
        Headers dictionary with Authorization header
    """
    return {"Authorization": f"Bearer {access_token}"}


def validate_required_params(params: Dict[str, Any], required: list) -> Optional[str]:
    """
    Validate that required parameters are present.
    
    Args:
        params: Dictionary of parameters to validate
        required: List of required parameter names
        
    Returns:
        Error message if validation fails, None if successful
    """
    missing = [param for param in required if param not in params or params[param] is None]
    if missing:
        return f"Missing required parameters: {', '.join(missing)}"
    return None 