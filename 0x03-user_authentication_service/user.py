#!/usr/bin/env python3
"""module to create a user SQLAlchemy"""
from SQLAlchemy import Column, Integer, String


class User(Base):
    """class to implement User"""
    __tablename__ = 'User'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    session_id = Column(String)
    reset_token = Column(String)