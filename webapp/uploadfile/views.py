from django import forms, urls
from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from .forms import UploadForms
from .models import UploadModel

# Create your views here.


class UploadFileView(CreateView):
    template_name = 'uploadfile/index.html'
    model = UploadModel
    # form_class = UploadForms
    fields = '__all__'
    success_url = '/uploadfile'


# class UploadFileView(View):
#     def get(self, request):
#         form = UploadForms
#         return render(request, 'uploadfile/index.html', {
#             'form': form
#         })

#     def post(self, request):
#         submitted_form = UploadForms(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             data = UploadModel(data=request.FILES['user_image'])
#             data.save()
#             return HttpResponseRedirect('/uploadfile')

#         return render(request, 'uploadfile/index.html', {
#             'form': submitted_form
#         })
