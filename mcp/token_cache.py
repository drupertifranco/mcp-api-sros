"""
Token cache management for Altiplano API authentication.
"""

import json
import os
import time
from typing import Optional, Dict, Any

try:
    from .config import TOKEN_CACHE_FILE, TOKEN_CACHE_DURATION
except ImportError:
    from config import TOKEN_CACHE_FILE, TOKEN_CACHE_DURATION

class TokenCache:
    """Manages authentication token caching."""
    
    def __init__(self, cache_file: str = TOKEN_CACHE_FILE):
        self.cache_file = cache_file
        self._cache_data = None
    
    def _load_cache(self) -> Dict[str, Any]:
        """Load cache data from file."""
        if self._cache_data is not None:
            return self._cache_data
            
        if not os.path.exists(self.cache_file):
            return {}
        
        try:
            with open(self.cache_file, 'r') as f:
                self._cache_data = json.load(f)
                return self._cache_data
        except (json.JSONDecodeError, IOError):
            return {}
    
    def _save_cache(self, data: Dict[str, Any]) -> None:
        """Save cache data to file."""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(data, f, indent=2)
            self._cache_data = data
        except IOError as e:
            print(f"Warning: Could not save token cache: {e}")
    
    def get_token(self) -> Optional[str]:
        """Get cached token if it's still valid."""
        cache = self._load_cache()
        
        if not cache:
            return None
        
        # Check if token exists and is not expired
        if 'access_token' in cache and 'expires_at' in cache:
            if time.time() < cache['expires_at']:
                return cache['access_token']
        
        return None
    
    def set_token(self, access_token: str, expires_in: int = 3600) -> None:
        """Cache a new token with expiration time."""
        cache_data = {
            'access_token': access_token,
            'expires_at': time.time() + expires_in,
            'cached_at': time.time()
        }
        self._save_cache(cache_data)
    
    def clear_cache(self) -> None:
        """Clear the token cache."""
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)
        self._cache_data = None
    
    def is_token_valid(self) -> bool:
        """Check if cached token is still valid."""
        return self.get_token() is not None
    
    def get_token_info(self) -> Dict[str, Any]:
        """Get information about the cached token."""
        cache = self._load_cache()
        if not cache:
            return {}
        
        info = {
            'has_token': 'access_token' in cache,
            'expires_at': cache.get('expires_at'),
            'cached_at': cache.get('cached_at'),
            'is_valid': self.is_token_valid()
        }
        
        if info['expires_at']:
            info['time_until_expiry'] = info['expires_at'] - time.time()
        
        return info

# Global token cache instance
token_cache = TokenCache()

def get_cached_token() -> Optional[str]:
    """Get cached token if available and valid."""
    return token_cache.get_token()

def cache_token(access_token: str, expires_in: int = 3600) -> None:
    """Cache a new token."""
    token_cache.set_token(access_token, expires_in)

def clear_token_cache() -> None:
    """Clear the token cache."""
    token_cache.clear_cache()

def is_token_cached() -> bool:
    """Check if a valid token is cached."""
    return token_cache.is_token_valid()

def get_token_info() -> Dict[str, Any]:
    """Get information about the cached token."""
    return token_cache.get_token_info() 