from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(reques):
    return HttpResponse("index of template engine")
