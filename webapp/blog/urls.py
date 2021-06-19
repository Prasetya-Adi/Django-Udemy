from django.urls import path

from . import views

urlpatterns = [
    path("contact", views.contact, name='HomeContact'),
    path("about", views.about, name='HomeAbout'),
    path("<titleURL>", views.post, name='HomePost'),
    path("", views.index, name='HomeBlog'),
]
