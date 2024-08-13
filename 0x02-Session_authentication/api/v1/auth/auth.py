#!/usr/bin/env python3
"""manage the API authentication"""
from flask import request
from typing import List, TypeVar
import re
import os


class Auth:
    """class to manage API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """path for authentication"""
        if path is not None and excluded_paths is not None:
            for i in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if i[-1] == '*':
                    pattern = '{}.*'.format(i[0:-1])
                elif i[-1] == '/':
                    pattern = '{}*'.format(i[0:-1])
                else:
                    pattern = '{}.*'.format(i)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization from header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method 3"""
        return None

    def session_cookie(self, request=None):
        """cookie value by request"""
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
