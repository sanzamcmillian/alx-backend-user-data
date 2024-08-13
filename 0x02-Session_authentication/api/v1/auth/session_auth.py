#!/usr/bin/env python3
"""session authorization"""
from auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """in session authorization class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method to create a session id"""
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
