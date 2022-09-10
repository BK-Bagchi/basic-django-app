from django.shortcuts import render
from django.http import HttpResponse


def MyDjangoApp(request):
    return HttpResponse("Hello World. This is basic django app to github")
