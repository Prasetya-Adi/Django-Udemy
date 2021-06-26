from django.urls import path
from . import views

urlpatterns = [
    path("list/<int:pk>", views.SingleReviewView.as_view(), name='one_Reviews'),
    path("list", views.ReviewListView.as_view(), name='listReviews'),
    path("you", views.thankyouView.as_view(), name='youReviews'),
    path("", views.ReviewView.as_view(), name='HomeReviews'),
]
