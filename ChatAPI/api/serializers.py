from rest_framework import serializers
from .models import Server,Channel,Message



class ServerSerial(serializers.ModelSerializer):
    lookup_field = 'post' 
    class Meta:
        model = Server
        fields="__all__"

class ChannelSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields="__all__"

class MessageSerial(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields=("user","body","message_channel",)