from django.shortcuts import render

# Create your views here.


def index(request):
    contex = {
        'judul': 'blog',
        'isi': 'ini blog',
    }
    return render(request, 'blog/index.html', contex)
