"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP(
    "Demo",    # Server name 
    "1.0.0"  # Server version
    )

# Add an addition tool
@mcp.tool()
def add_ip(prefix_name: str, prefix: str) -> dict:
    """Agrega un prefijo IP usando la API FastAPI"""
    url = "http://localhost:8000/add-ip"
    payload = {
        "prefix_name": prefix_name,
        "prefix": prefix
    }
    response = requests.post(url, json=payload)
    return response.json()

@mcp.tool()
def delete_ip(prefix_name: str, prefix: str) -> dict:
    """Elimina un prefijo IP usando la API FastAPI"""
    url = "http://localhost:8000/delete-ip"
    payload = {
        "prefix_name": prefix_name,
        "prefix": prefix
    }
    response = requests.delete(url, json=payload)
    return response.json()

@mcp.tool()
def get_public_ip() -> dict: 
    """Obtiene la IP pública del servidor"""
    ip = requests.get(url='https://ifconfig.me/all.json').text
    return {"public_ip": ip}
    

# Start the MCP server
if __name__ == "__main__":
    mcp.run()   
# This code sets up a FastMCP server that can interact with a FastAPI application
# to add and delete IP prefixes. The server listens for requests and forwards them  
# to the FastAPI endpoints defined in the `src/routers/ip_router.py` file.
# The `add_ip` and `delete_ip` functions are decorated with `@mcp.tool()` to make them
# available as tools in the MCP server. The server can be run using the command:        
# `uv run server fastmcp_quickstart stdio` from the command line.