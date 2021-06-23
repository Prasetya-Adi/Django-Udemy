from django.urls import path

from . import views

urlpatterns = [
    path("author/<author>", views.author, name='SecondBlogPostAuthor'),
    path("contact", views.contact, name='SecondBlogContact'),
    path("about", views.about, name='SecondBlogAbout'),
    path("<slug:slug>", views.post, name='SecondBlogPost'),
    path("", views.index, name='SecondBlog'),
]
