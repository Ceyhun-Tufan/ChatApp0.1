from rest_framework import serializers
from .models import Server,Channel,Message



class ServerSerial(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields="__all__"

class ChannelSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields="__all__"

class MessageSerial(serializers.ModelSerializer):
    username = serializers.CharField(source="user.user_name")
    class Meta:
        model = Message
        fields=("user","body","message_channel","username",)