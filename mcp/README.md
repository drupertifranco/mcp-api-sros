# Modular MCP Server for Altiplano API

This directory contains a modular FastMCP server implementation for interacting with Nokia Altiplano API endpoints.

## Architecture

The server is organized into a modular structure for better maintainability and scalability:

```
mcp/
├── __init__.py              # Package initialization
├── config.py                # Configuration settings and constants
├── utils.py                 # Utility functions and helpers
├── server_factory.py        # MCP instance management
├── server.py               # Main server entry point
├── README.md               # This documentation
└── tools/                  # Tool modules by category
    ├── __init__.py         # Tools package initialization
    ├── auth_tools.py       # Authentication tools
    ├── delete_tools.py     # Delete operations
    ├── create_tools.py     # Create operations (ONT & L2-User)
    ├── get_tools.py        # Get/Read operations
    ├── infrastructure_tools.py  # Infrastructure operations
    ├── sync_tools.py       # Synchronization operations
    └── legacy_tools.py     # Legacy FastAPI endpoints
```

## Module Descriptions

### Core Modules

- **`config.py`**: Centralized configuration including URLs, headers, default values, and constants
- **`utils.py`**: Common utility functions for HTTP requests, authentication, and validation
- **`server_factory.py`**: Manages the global MCP instance across modules
- **`server.py`**: Main entry point that creates the MCP server and imports all tools

### Tool Modules

#### `auth_tools.py`
- `get_access_token()`: Authenticate and get access/refresh tokens

#### `delete_tools.py`
- `delete_internet()`: Delete Internet intent
- `delete_ont()`: Delete ONT intent
- `delete_infrastructure()`: Delete L2 infrastructure intent

#### `create_tools.py`
- `add_ont_bridge()`: Add ONT with bridge type
- `add_ont_transparent()`: Add ONT with transparent type
- `add_l2_user_hsi()`: Add L2-User with HSI configuration
- `add_l2_user_untagged()`: Add L2-User with untagged configuration
- `add_l2_user_transparent()`: Add L2-User with transparent configuration

#### `get_tools.py`
- `get_l2_user()`: Get L2-User information

#### `infrastructure_tools.py`
- `create_residential_bridge_transparent()`: Create residential bridge infrastructure
- `create_cross_connect()`: Create cross-connect infrastructure
- `create_s_vlan_cross_connect()`: Create S-VLAN cross-connect infrastructure

#### `sync_tools.py`
- `sync_device_config()`: Synchronize device configuration

#### `legacy_tools.py`
- `add_ip()`: Add IP prefix (existing FastAPI endpoint)
- `delete_ip()`: Delete IP prefix (existing FastAPI endpoint)
- `get_public_ip()`: Get public IP address

## Benefits of Modular Structure

1. **Maintainability**: Each module has a single responsibility
2. **Scalability**: Easy to add new tool categories
3. **Reusability**: Common utilities and configurations are shared
4. **Testing**: Individual modules can be tested in isolation
5. **Documentation**: Clear organization makes it easier to understand
6. **Team Development**: Multiple developers can work on different modules

## Adding New Tools

To add new tools:

1. **Create a new tool module** in `tools/` directory
2. **Import the MCP instance** using `from ..server_factory import get_mcp_instance`
3. **Use the utility functions** from `utils.py` for consistent behavior
4. **Add configuration** to `config.py` if needed
5. **Import the new tools** in `server.py`
6. **Update this README** with documentation

## Configuration

All configuration is centralized in `config.py`:

- Base URLs for different APIs
- Default headers and authentication
- Default values for parameters
- Intent type versions
- Service profiles

## Error Handling

The `utils.py` module provides consistent error handling across all tools:

- HTTP request errors are caught and returned as structured responses
- Validation functions ensure required parameters are present
- All tools return dictionaries with consistent structure

## Usage

Run the server using:

```bash
cd examples/snippets/clients
uv run server fastmcp_quickstart stdio
```

The server will automatically load all tools from the modular structure and make them available for use. 