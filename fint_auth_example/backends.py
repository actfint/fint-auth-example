from typing import Dict, List, Optional, Tuple

from fastapi import WebSocket
from starlette.requests import Request

from fint_rtc_server.model.user import User


class User(User):
    pass


def current_user(*args, **kwargs):
    async def _(
        request: Request = None,
        websocket: WebSocket = None,
    ):
        return User(user_id='anonymous')

    return _


def websocket_auth(permissions: Optional[Dict[str, List[str]]] = None):
    async def _(
        websocket: WebSocket,
    ) -> Optional[Tuple[WebSocket, Optional[Dict[str, List[str]]]]]:
        return websocket, permissions

    return _


async def update_user():
    async def _(*args, **kwargs):
        pass

    return _
