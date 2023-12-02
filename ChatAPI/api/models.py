from django.db import models
from django.contrib.auth.models import User

# server->channel->messages
# class type:
# user
# ... details
# time model fields

class Server(models.Model):
    owner = models.ForeignKey(User,on_delete=models.SET_DEFAULT,default="None") # if owner got deleted, its just None
    name = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    server_profile = models.ImageField(upload_to ='uploads/% Y/% m/% d/',default=None,blank=True)  # uploading to daily created folder

    def __str__(self) -> str:
        return str(self.name)

class Channel(models.Model):
    server = models.ForeignKey(Server,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.name)


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=400)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    message_channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.body[:20])