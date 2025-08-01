"""
MCP server factory for managing the FastMCP instance across modules.
"""

from mcp.server.fastmcp import FastMCP

# Global MCP instance
_mcp_instance = None


def get_mcp_instance() -> FastMCP:
    """
    Get the global MCP instance, creating it if it doesn't exist.
    
    Returns:
        FastMCP instance
    """
    global _mcp_instance
    if _mcp_instance is None:
        _mcp_instance = FastMCP(
            "Altiplano API Tools",
            "1.0.0"
        )
    return _mcp_instance


def set_mcp_instance(instance: FastMCP) -> None:
    """
    Set the global MCP instance.
    
    Args:
        instance: FastMCP instance to set
    """
    global _mcp_instance
    _mcp_instance = instance 