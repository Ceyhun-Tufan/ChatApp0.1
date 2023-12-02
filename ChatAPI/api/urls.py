from django.urls import path,include
from rest_framework import routers
from .views import home_view,server_view,channel_view,MessageView,ChannelView,ServerView,send,getMessages

router = routers.DefaultRouter()

router.register(r'message-data',MessageView)
router.register(r'channel-data',ChannelView)
router.register(r'server-data',ServerView)




urlpatterns = [
    path("",home_view,name="home"),
    path("server/<str:sk>/",server_view,name="server"),
    path("channel/<str:ck>/",channel_view,name="channel"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/",include(router.urls)),
    path('send', send, name='send'),
    path('getMessages/<str:channel>/', getMessages, name='getMessages'),

]