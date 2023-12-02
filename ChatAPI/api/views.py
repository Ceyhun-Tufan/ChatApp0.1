from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Server,Channel,Message,User
from rest_framework import viewsets
from .serializers import *
# Create your views here.

def home_view(requests):
    contents = {
        "contents":Server.objects.all()          # listing all the servers in the main page
    }
    return render(requests,"home.html",contents)
    

def server_view(requests,sk):
    contents = {
        "contents" :Channel.objects.all().filter(server = sk)
        }
    
    return render(requests,"server.html",contents)

def channel_view(requests,ck):
    contents = {
        "contents" : Message.objects.all().filter(message_channel=ck)
        }
    contents = {
        "channel_content":Channel.objects.get(id=ck),
        "message_content" :Message.objects.all().filter(message_channel=ck)
        }
    return render(requests,"channel.html",contents)



def send(request):
    body = request.POST['message']
    user_id = request.POST['user_id']
    channel_id = request.POST['room_id']

    new_message = Message.objects.create(body=body, user=User.objects.get(id=user_id), message_channel=Channel.objects.get(id=channel_id))
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, channel):
    channel_details = Channel.objects.get(id=channel)
    messages = Message.objects.filter(message_channel=channel_details)
    # message_values = messages.values()
    # message_values["user_id"] = User.objects.all().filter(id = message_values["user_id"]) queryde olmuyor
    return JsonResponse({"messages":list(messages.values())})





class ServerView(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerial
        
class ChannelView(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerial

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerial
