# FastAPI IP Router

This project is a FastAPI and MCP Server application that provides an interface with Claude LLM for managing IP prefixes on a Nokia SROS device. It allows users to add and delete IP prefixes through HTTP endpoints. The application is designed for future integration with n8n for workflow automation.

## Project Structure

```
fastapi-ip-router
├── mcp
│   ├── server.py  
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── routers
│   │   └── ip_router.py       # API routes for adding and deleting IP addresses
│   ├── services
│   │   └── sros_service.py     # Logic for connecting to the SROS device
│   └── types
│       └── index.py           # Custom types and data models
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
``` 

## Setup Instructions 

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-ip-router
   ```
   **Setup you proyect**

   In file:

    ```
    fastapi-ip-router
    ├── src
    │   ├── services
    │   │   └── sros_service.py     # Logic for connecting to the SROS device
    ```
    Put your credencial and IP of router

   ```
   conn = connect(host="########PUT_YOUR_IP_HERE########",
                       username="########PUT_YOUR_USER_HERE########",
                       password="########PUT_YOUR_PASSWORD_HERE########",
                       hostkey_verify=False)
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   uvicorn src.main:app --reload
   ```
5. **Inspector MCP**
    ```
    uv run mcp dev server.py
      ```
## Usage

- **Get Public IP:**
  - Endpoint: `get`
  - Request Body:
    ```json
    {
      N/A
    }
    ```

- **Add IP Prefix:**
  - Endpoint: `POST /ip-prefix`
  - Request Body:
    ```json
    {
      "prefix-name": "xyz"
      "prefix": "1.1.1.1/32"
    }
    ```

- **Delete IP Prefix:**
  - Endpoint: `DELETE /ip-prefix`
  - Request Body:
    ```json
    {
      "prefix-name": "xyz"
      "prefix": "1.1.1.1/32"
    }
    ```
## LM studio config MCP

- **MCP Config**
    ```json
      {
      "mcpServers": {
        "Demo": {
          "command": "uv",
          "args": [
            "run",
            "C:/Users/.../fastapi-ip-router/mcp/server.py"
          ]
        }
      }
    }
    ```

## Future Integration with n8n or LLM

This FastAPI application is designed to be easily integrated with n8n, allowing for automated workflows that can manage IP prefixes on the SROS device. Further documentation on integration will be provided as the project evolves.