from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField, SlugField

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True, unique=True)
    content = models.TextField(max_length=100000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}'
