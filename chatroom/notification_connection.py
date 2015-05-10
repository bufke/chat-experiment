from swampdragon_notifications.notification_connection import Connection
from swampdragon_notifications.online import (
    user_manager, redis_user_manager, mock_user_manager)
from chatroom.models import Profile
import sys


def manager():
    if 'test' in sys.argv:
        return mock_user_manager
    return redis_user_manager


def add_user(id):
    manager().add_user(id)


def remove_user(id):
    manager().remove_user(id)


class ChatConnection(Connection):
    def on_open(self, request):
        print(request)
        super(Connection, self).on_open(request)

    def on_heartbeat(self):
        print('heartbeat!!!!!!!!!!!!')
        if self.user:
            user_manager.add_user(self.user.pk)
        super(Connection, self).on_heartbeat()
