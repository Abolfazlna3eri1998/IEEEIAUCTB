from django.http import HttpResponse, request
from django.shortcuts import render


def index(request):
    return render(request, "base.html", {})


def homepage(request):
    return render(request, "index.html")


def register(request):
    return render(request, "registerform.html")


def contactus(request):
    return render(request, "tamasbama.html")
