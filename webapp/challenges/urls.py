from django.urls import path
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<bulan>[\w-]+)/$', views.Random),
    path('v2/<bulan2>', views.Random2),
    path('v2/<int:bulan2>', views.Random3),
]
