from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.


def index(request):
    contex = {
        'title': 'Reviews',
        'has_error': False,
    }

    if request.method == "POST":
        entered_username = request.POST['username']
        entered_review = request.POST['review']

        if entered_username == '':
            return render(request, 'reviews/index.html',  {
                'has_error': True,
            })

        print(entered_username)
        print(entered_review)
        return HttpResponseRedirect('/reviews/you')

    return render(request, 'reviews/index.html', contex)


def you(request):
    contex = {
        'title': 'Thank You',
    }
    return render(request, 'reviews/thankyou.html', contex)
