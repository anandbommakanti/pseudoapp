from django.shortcuts import render
from django.http import HttpResponse

def demoapp(request):
    return HttpResponse("Hi, This is a Pseudo Application. Version: 1.0")