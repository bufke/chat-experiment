from swampdragon_auth.socketconnection import HttpDataConnection
from .online import user_manager
from chatroom.models import Profile


class ChatConnection(HttpDataConnection):
    def __init__(self, session):
        self._user = None
        super().__init__(session)

    def on_heartbeat(self):
        if self.user:
            user_manager.add_user(self.user.pk)
        super().on_heartbeat()

    def on_open(self, request):
        super().on_open(request)

    def on_close(self):
        super().on_close()
        user_manager.remove_user(self.user.pk)
