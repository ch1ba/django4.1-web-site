from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Simple.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'cat_selected': 0,
        'title': 'Главная страница',
    }

    return render(request, 'simple/index.html', context=context)

def show_category(request, cat_id):
    posts = Simple.objects.filter(cat_id = cat_id)
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение категорий',
        'cat_selected': cat_id,
    }
    if len(posts) == 0:
        raise Http404

    return render(request, 'simple/index.html', context=context)

def about(request):
    dictionary = {
        "menu": menu,
        "cats": Category.objects.all(),
        "title": "О сайте"
    }
    return render(request, 'simple/about.html', context=dictionary)


def addpage(request):
    dictionary = {
        "menu": menu,
        "cats": Category.objects.all(),
    }
    return render(request,"simple/page_add.html",context=dictionary)

def contact(request):
    dictionary = {
        "menu": menu,
        "cats": Category.objects.all(),
    }
    return render(request,"simple/contact.html",context=dictionary)

def login(request):
    dictionary = {
        "menu": menu,
        "cats": Category.objects.all(),
    }
    return render(request,"simple/login.html",context=dictionary)


def page_not(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

