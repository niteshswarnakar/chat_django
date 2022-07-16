from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Room 
from .forms import RoomForm

# rooms = [
#         {'id':'1','name':'Lets learn graphic design'},
#         {'id':'2','name':'Beginner for backend development'},
#         {'id':'3','name':'Learning Machine Learning'},
# ]

def home(request):
        rooms = Room.objects.all()
        context = {'rooms':rooms}
        return render(request, 'home.html',context)

def getrooms(request):
        rooms = Room.objects.all()
        context = {'rooms':rooms}
        return render(request, 'rooms.html',context)

def getroom(request,pk):
        room = Room.objects.get(id = pk)
        
        return render(request, 'room.html',{'room':room})

def createRoom(request):
        form = RoomForm()
        if request.method == 'POST':
                # print(request.body.get('description'))
                form = RoomForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('home')
        context = {'form':form}
        return render(request, 'forms.html',context)


def udpateRoom(request,pk):
        room = Room.objects.get(id = pk)
        form = RoomForm(instance = room)

        if request.method == 'POST':
                form = RoomForm(request.POST, instance = room)
                if form.is_valid():
                        form.save()
                        return redirect('home')

        context = {'form':form}
        return render(request,"forms.html",context)








