from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg, Min, Max
from .models import Book
# Create your views here.

books = Book.objects.all().order_by('title')
num_books = Book.objects.count()
avg_rating = Book.objects.aggregate(Avg("rating"))


def index(request):
    context = {
        'all_book': books,
        'num_books': num_books,
        'avg_rating': avg_rating,
    }
    return render(request, 'relationships/index.html', context)


def databooks(request, slug):
    # try:
    #     a_book = Book.objects.get(title=slug)
    # except:
    #     raise Http404()

    a_book = get_object_or_404(Book, slug=slug)
    context = {
        'a_book': a_book
    }
    return render(request, 'relationships/detail.html', context)
