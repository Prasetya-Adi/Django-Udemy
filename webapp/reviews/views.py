from django.db.models.base import Model
from django.forms.forms import Form
import reviews
from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


from .forms import ReviewForms
from .models import Review

# Create your views here.

# FIRST OPTION
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForms()
#         return render(request, 'reviews/index.html', {'title': "Reviews", 'form': form})

#     def post(self, request):
#         form = ReviewForms(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/reviews/you')
#         return render(request, 'reviews/index.html', {'title': "Reviews", 'form': form})


# SECOND OPTION
# class ReviewView(FormView):
#     form_class = ReviewForms
#     template_name = 'reviews/index.html'
#     success_url = '/reviews/you'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# THIRD OPTION
class ReviewView(CreateView):
    Model = Review
    form_class = ReviewForms
    template_name = 'reviews/index.html'
    success_url = '/reviews/you'


class thankyouView(TemplateView):
    template_name = 'reviews/thankyou.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Thank You'
        return contex


# class ReviewListView(TemplateView):
#     template_name = 'reviews/review_list.html'

#     def get_context_data(self, **kwargs):
#         review = Review.objects.all()
#         contex = super().get_context_data(**kwargs)
#         contex['form'] = review
#         return contex


# ListView for show the list of database in an easy way
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # query for getting more than 4
    def get_queryset(self):
        basequery = super().get_queryset()
        data = basequery.filter(rating__gt=4)
        return data


# class SingleReviewView(TemplateView):
#     template_name = 'reviews/single_review.html'

#     def get_context_data(self, **kwargs):
#         review_id = kwargs['id']
#         review = Review.objects.get(pk=review_id)
#         contex = super().get_context_data(**kwargs)
#         contex['review'] = review
#         return contex

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
