from rest_framework import serializers
from .models import Message, Room, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'display_name')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('user',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
