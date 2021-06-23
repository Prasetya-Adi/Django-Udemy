from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    contex = {
        'title': 'Reviews'
    }
    return render(request, 'reviews/index.html', contex)
