from django.shortcuts import render
from django.http import HttpResponse 


rooms = [
        {'id':'1','name':'Lets learn graphic design'},
        {'id':'2','name':'Beginner for backend development'},
        {'id':'3','name':'Learning Machine Learning'},
]

def home(request):
        return render(request, 'home.html',{'rooms':rooms})

def getrooms(request):
        return render(request, 'rooms.html',{'rooms':rooms})

def getroom(request,pk):
        return render(request, 'room.html',{'room':rooms[int(pk)-1]})
