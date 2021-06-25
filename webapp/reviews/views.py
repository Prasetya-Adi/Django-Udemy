from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import ReviewForms
from .models import Review

# Create your views here.


def index(request):
    if request.method == "POST":
        form = ReviewForms(request.POST)

        if form.is_valid():
            review = Review(user_name=form.cleaned_data['user_name'],
                            review_text=form.cleaned_data['review_text'],
                            rating=form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect('/reviews/you')

    else:
        form = ReviewForms()
    return render(request, 'reviews/index.html', {'title': "Reviews", 'form': form})


def you(request):
    contex = {
        'title': 'Thank You',
    }
    return render(request, 'reviews/thankyou.html', contex)
