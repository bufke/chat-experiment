from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from swampdragon_notifications.routers import OnlineUsersRouter
from .models import Message, Profile
from .dragon_serializers import MessageSerializer, UserSerializer
from .connection.online import user_manager


class MessageRouter(ModelRouter):
    route_name = 'messages'
    serializer_class = MessageSerializer
    model = Message
    paginate_by = 50

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def get_subscription_contexts(self, **kwargs):
        return {'room__users__pk': self.connection.user.pk}


class UserRouter(ModelRouter):
    route_name = 'users'
    serializer_class = UserSerializer
    model = Profile

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def subscribe(self, **kwargs):
        print('I will subscribe')
        return super().subscribe(**kwargs)


route_handler.register(MessageRouter)
route_handler.register(UserRouter)


# Modified OnlineUsersRouter
class ChatOnlineUsersRouter(OnlineUsersRouter):
    def subscribe(self, **kwargs):
        if not self.connection.user:
            return

        #super().subscribe(**kwargs)
        if self.connection.user:
            print('chat online user router ohhhhhh add the user pls')
            user_manager.add_user(self.connection.user.pk)
route_handler.registered_handlers['swampdragon-online'] = ChatOnlineUsersRouter
