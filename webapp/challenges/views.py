from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Januari(request):
    return HttpResponse("ini Januari")


def Februari(request):
    return HttpResponse("ini Februari")
