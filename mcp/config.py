"""
Configuration settings for the MCP server.
"""

import os
from typing import Optional

# Base configuration
BASE_URL = "http://192.168.9.65/nokia-altiplano-ac"
DEFAULT_HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# FastAPI configuration
FASTAPI_BASE_URL = "http://localhost:8000"

# Authentication configuration
# You can set these via environment variables or modify them directly
ALTIPLANO_USERNAME = os.getenv("ALTIPLANO_USERNAME", "admin")  # Default username
ALTIPLANO_PASSWORD = os.getenv("ALTIPLANO_PASSWORD", "admin")  # Default password

# Token cache configuration
TOKEN_CACHE_DURATION = 3600  # Token cache duration in seconds (1 hour)
TOKEN_CACHE_FILE = ".token_cache.json"  # File to store cached token

# Default values
DEFAULT_TARGETS = {
    "internet": "HSI#MED-03",
    "ont": "MED-03",
    "infrastructure": "OLT1#HSI",
    "l2_user": "HSI#MED-03"
}

DEFAULT_SERIAL_NUMBER = "ALCLFCA06F4B"
DEFAULT_FIBER_NAME = "PON1_OLT1"
DEFAULT_NNI_ID = "nt-a:xfp:1"

# Intent type versions
INTENT_VERSIONS = {
    "ont": "10",
    "l2_user": "13",
    "l2_infra": "12"
}

# Service profiles
SERVICE_PROFILES = {
    "internet": "INTERNET_TC0",
    "speed": "PLAN_100M",
    "unicast": "Unicast",
    "unicast_l2cp": "Unicast-l2cp-pass"
}

# SSL Configuration
VERIFY_SSL = False  # Set to True in production with proper certificates 