from rest_framework import viewsets
from .serializers import MessageSerializer, RoomSerializer
from .models import Message, Room


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(room__organization__users=user)


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(organization__users=user)
