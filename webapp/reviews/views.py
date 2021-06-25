from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import ReviewForms

# Create your views here.


def index(request):
    if request.method == "POST":
        form = ReviewForms(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/reviews/you')

    else:
        form = ReviewForms()
    return render(request, 'reviews/index.html', {'title': "Reviews", 'form': form})


def you(request):
    contex = {
        'title': 'Thank You',
    }
    return render(request, 'reviews/thankyou.html', contex)
