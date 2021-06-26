from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForms

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForms()
        return render(request, 'reviews/index.html', {'title': "Reviews", 'form': form})

    def post(self, request):
        form = ReviewForms(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reviews/you')
        return render(request, 'reviews/index.html', {'title': "Reviews", 'form': form})


class thankyouView(TemplateView):
    template_name = 'reviews/thankyou.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Thank You'
        return contex
