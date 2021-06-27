from django.urls import path
from . import views

urlpatterns = [
    path("", views.UploadFileView.as_view(), name='HomeUploadFile'),
    path("all", views.allimage.as_view()),
]
