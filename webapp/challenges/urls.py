from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name='Homechallenges'),
    re_path(r'^(?P<bulan>[\w-]+)/$', views.Random1, name='bulanreverse'),
    path('v2/<bulan>', views.Random2),
    path('v3/<bulan>', views.Random3),
    path('v4/<int:bulan>', views.Random4),
    path('v5/<int:bulan>', views.Random5),
]
