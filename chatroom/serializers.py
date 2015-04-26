from rest_framework import serializers
from .models import Message, Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('user',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
