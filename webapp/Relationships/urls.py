from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='HomeRelationships'),
    path("<slug>", views.databooks, name='DetailRelationships'),
]
