from django.db import models
from django.db.models.base import Model

# Create your models here.


class UploadModel(models.Model):
    data = models.ImageField(upload_to='data')
