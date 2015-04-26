from swampdragon.serializers.model_serializer import ModelSerializer


class MessageSerializer(ModelSerializer):
    class Meta:
        model = 'chatroom.Message'
        publish_fields = ('user', 'text', 'posted')
