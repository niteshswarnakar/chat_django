
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello developers")

def room(request):
    return HttpResponse("I am in room")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    
]
