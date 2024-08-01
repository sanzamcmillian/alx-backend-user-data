#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Method to encrypt a password"""
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
