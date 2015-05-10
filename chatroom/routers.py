from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from .models import Message, Profile
from .dragon_serializers import MessageSerializer, UserSerializer


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


class UserSerializer(ModelRouter):
    route_name = 'users'
    serializer_class = UserSerializer
    model = Profile

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(MessageRouter)
