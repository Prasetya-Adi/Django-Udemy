from django.urls import path
from . import views

urlpatterns = [
    path("you", views.thankyouView.as_view(), name='youReviews'),
    path("", views.ReviewView.as_view(), name='HomeReviews'),
]
