from django.shortcuts import render
from .models import Chatroom_message
from edu.models import Tutor

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    current_user = Tutor.objects.get(user=request.user)
    room_name = str(room_name)
    chat_log = ""
    if Chatroom_message.objects.filter(room_name=room_name).exists() :
       chat_log = Chatroom_message.objects.get(room_name=room_name).message

    return render(request, 'chat/room.html', {
        'room_name': room_name ,
        'chat_log' : chat_log,
        'current_user': current_user,
    })
