#!/usr/bin/env python3
"""manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method 1"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """method 2"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """method 3"""
        return None
