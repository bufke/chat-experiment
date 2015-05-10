from django.db.models import Q
from rest_framework import viewsets
from .serializers import MessageSerializer, RoomSerializer, ProfileSerializer
from .models import Message, Room, Profile


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user.profile
        return qs.filter(
            Q(organization__users=user) | Q(room__users=user)).distinct()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_fields = ('room',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user.profile
        return qs.filter(room__users=user)


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_queryset(self):
        user = self.request.user.profile
        return Room.objects.filter(
            Q(organization__users=user) | Q(users=user)).distinct()
