from django.urls import path , include 
from django.http import HttpResponse

from . import views

urlpatterns = [
        path("",views.home, name = "home"),
        path('rooms/',views.getrooms, name = "rooms"),
        path('rooms/<str:pk>/',views.getroom, name = "room"),
]