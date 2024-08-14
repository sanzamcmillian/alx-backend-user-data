#!/usr/bin/env python3
"""module to authentication"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """method to hash a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
