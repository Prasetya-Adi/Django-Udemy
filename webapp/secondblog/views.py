from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Author

# Create your views here.

isiblog = Post.objects.all()


def index(request):
    contex = {
        'heading': 'a Simple Blog',
        'subheading': 'A Blog by Prasetya Adi',
        'urlBackgroud': 'assets/img/home-bg.jpg',
        'isiblog': isiblog,
    }
    return render(request, 'secondblog/index.html', contex)


def post(request, slug):
    # content = Post.objects.get(slug=slug)
    content = get_object_or_404(Post, slug=slug)
    contex = {
        'isiblog': content,
        'post_tag': content.tag.all()
    }
    return render(request, 'secondblog/post.html', contex)


def author(request, author):
    author_post = Post.objects.filter(author__first_name=author)
    contex = {
        'heading': 'a Simple Blog',
        'subheading': 'A Blog by Prasetya Adi',
        'urlBackgroud': 'assets/img/home-bg.jpg',
        'isiblog': author_post,
    }
    return render(request, 'secondblog/author.html', contex)


def about(request):
    contex = {
        'heading': 'About Me',
        'subheading': 'This is what I do.',
        'urlBackgroud': 'assets/img/about-bg.jpg',
    }
    return render(request, 'secondblog/about.html', contex)


def contact(request):
    contex = {
        'heading': 'Contact Me',
        'subheading': 'Have questions? I have answers.',
        'urlBackgroud': 'assets/img/contact-bg.jpg',
    }
    return render(request, 'secondblog/contact.html', contex)
