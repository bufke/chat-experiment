from django.contrib import admin
from .models import Message, Room, Organization, Profile


admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Organization)
admin.site.register(Profile)
