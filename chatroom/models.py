from django.db import models
from swampdragon.models import SelfPublishModel
from allauth.account.signals import user_signed_up
from .dragon_serializers import MessageSerializer


class Profile(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True)
    display_name = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)
    status = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.display_name

    @staticmethod
    def create_profile(request, user, **kwargs):
        return Profile.objects.create(
            user=user,
            display_name='{}.{}'.format(
                user.first_name, user.last_name).strip('.'),
        )

user_signed_up.connect(Profile.create_profile)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    users = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=75)
    organization = models.ManyToManyField(Organization, blank=True)
    users = models.ManyToManyField(
        Profile,
        help_text="Users in this room. May include non organization users.")
    is_active = models.BooleanField(default=True)
    add_by_default = models.BooleanField(
        default=True,
        help_text="Organization users will automatically join this room.")

    def __str__(self):
        return self.name


class Message(SelfPublishModel, models.Model):
    serializer_class = MessageSerializer
    user = models.ForeignKey('auth.User')
    text = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return '{}: {}'.format(self.user, self.text)
