from swampdragon_notifications.notification_connection import Connection
from swampdragon_auth.socketconnection import HttpDataConnection
from .online import user_manager
from chatroom.models import Profile


class ChatConnection(Connection):
    def on_open(self, request):
        super().on_open(request)

    def on_close(self):
        print('close it')
        super().on_close()

    def on_heartbeat(self):
        if self.user:
            user_manager.add_user(self.user.pk)
