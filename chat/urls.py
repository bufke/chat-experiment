from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from chatroom import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'rooms', views.RoomViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
