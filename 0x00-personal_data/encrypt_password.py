#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Method to encrypt a password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
