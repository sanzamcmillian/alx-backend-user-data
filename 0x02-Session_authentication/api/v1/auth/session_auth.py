#!/usr/bin/env python3
"""session authorization module"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """session authorization class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method to create a session id for the user"""
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """id user based on session id"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
