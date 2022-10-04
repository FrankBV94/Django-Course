from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(requuest):
    return HttpResponse("Index page")


def aloha(request, username):
    print(username)
    return HttpResponse("<h1>Aloha %s<h1>" % username)


def about(request):
    return HttpResponse("<h1>About<h1>")
