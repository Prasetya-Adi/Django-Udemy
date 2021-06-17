from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path("Januari", views.Januari),
    path("Februari", views.Februari),
]
