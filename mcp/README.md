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

- **`config.py`**: Centralized configuration including URLs, headers, default values, credentials, and constants
- **`utils.py`**: Common utility functions for HTTP requests, authentication, and validation
- **`token_cache.py`**: Token caching system for automatic authentication
- **`server_factory.py`**: Manages the global MCP instance across modules
- **`server.py`**: Main entry point that creates the MCP server and imports all tools

### Tool Modules

#### `auth_tools.py`
- `get_access_token()`: Authenticate and get access/refresh tokens (uses cached token if available)
- `get_cached_token_info()`: Get information about cached token
- `clear_cached_token()`: Clear the cached authentication token
- `authenticate_with_cached_token()`: Convenience function for automatic authentication

#### `delete_tools.py`
- `delete_internet()`: Delete Internet intent (auto-auth)
- `delete_ont()`: Delete ONT intent (auto-auth)
- `delete_infrastructure()`: Delete L2 infrastructure intent (auto-auth)

#### `create_tools.py`
- `add_ont_bridge()`: Add ONT with bridge type
- `add_ont_transparent()`: Add ONT with transparent type
- `add_l2_user_hsi()`: Add L2-User with HSI configuration
- `add_l2_user_untagged()`: Add L2-User with untagged configuration
- `add_l2_user_transparent()`: Add L2-User with transparent configuration

#### `get_tools.py`
- `get_l2_user()`: Get L2-User information (auto-auth)

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
- **User credentials** (can be set via environment variables)
- **Token cache settings** (duration, file location)
- Default values for parameters
- Intent type versions
- Service profiles

### Environment Variables

You can set credentials via environment variables:
```bash
export ALTIPLANO_USERNAME="your_username"
export ALTIPLANO_PASSWORD="your_password"
```

Or modify them directly in `config.py`.

## Authentication & Token Caching

The server includes a comprehensive authentication system:

### Automatic Token Management
- **Token Caching**: Tokens are automatically cached and reused
- **Auto-Authentication**: Tools automatically use cached tokens when no `access_token` is provided
- **Token Expiration**: Cached tokens expire after 1 hour (configurable)
- **Cache Persistence**: Tokens are saved to disk and persist between sessions

### Authentication Tools
- `get_access_token()`: Get token (uses cached if available)
- `authenticate_with_cached_token()`: Automatic authentication
- `get_cached_token_info()`: Check token status
- `clear_cached_token()`: Clear cached token

### Usage Examples
```python
# Automatic authentication (uses cached token or default credentials)
result = get_l2_user()  # No access_token needed

# Manual authentication
token_result = get_access_token("username", "password")
result = get_l2_user(access_token=token_result["access_token"])

# Check token status
info = get_cached_token_info()
```

## Error Handling

The `utils.py` module provides consistent error handling across all tools:

- HTTP request errors are caught and returned as structured responses
- Validation functions ensure required parameters are present
- Authentication errors provide clear guidance on how to authenticate
- All tools return dictionaries with consistent structure

## Usage

### Running the Server

You can run the server in several ways:

#### Option 1: Using the standalone server (Recommended)
```bash
cd mcp
python standalone_server.py
```

#### Option 2: Using the MCP dev command
```bash
cd mcp
uv run mcp dev standalone_server.py
```

#### Option 3: Testing the server
```bash
cd mcp
python test_server.py
```

#### Option 4: Testing authentication
```bash
cd mcp
python test_auth.py
```

### File Structure for Running

- **`standalone_server.py`**: Standalone server that can be executed directly (Recommended)
- **`server.py`**: Modular server (requires proper Python path setup)
- **`run_server.py`**: Alternative standalone runner
- **`test_server.py`**: Test script to verify the server works correctly

The server will automatically load all tools from the modular structure and make them available for use. 