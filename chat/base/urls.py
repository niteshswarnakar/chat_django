from django.urls import path , include 
from django.http import HttpResponse

from . import views

urlpatterns = [
        path("",views.home, name = "home"),
        path('rooms/',views.getrooms, name = "rooms"),
        path('rooms/<str:pk>/',views.getroom, name = "room"),
        path("create-room/",views.createRoom, name = "create-room"),
        path("udpate-room/<str:pk>/",views.udpateRoom, name = "udpate-room"),
        path("delete-room/<str:pk>/",views.deleteRoom, name = "delete-room"),
        path("greet/",views.greet, name = "greet")
]