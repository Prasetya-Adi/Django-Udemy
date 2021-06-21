from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='HomeData'),
    path("<slug>", views.databooks, name='DataBooks'),
]
