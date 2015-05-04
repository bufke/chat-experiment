from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from rest_framework import routers
from chatroom import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'users', views.ProfileViewSet)


urlpatterns = patterns('',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(
        TemplateView.as_view(template_name='index.html')
    ), name='home'),
)
