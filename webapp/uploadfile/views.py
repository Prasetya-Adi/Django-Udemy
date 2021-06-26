from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class UploadFileView(TemplateView):
    template_name = 'uploadfile/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Upload Your File'
        return contex
