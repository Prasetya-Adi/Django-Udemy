from django.urls import path
from . import views

urlpatterns = [
    path("you", views.you, name='youReviews'),
    path("", views.index, name='HomeReviews'),
]
