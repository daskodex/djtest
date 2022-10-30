from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *

menu = [{'title' : 'О сайте', 'url_name' : 'about'},
        {'title' : 'Добавить статью', 'url_name' : 'add_page'},
        {'title' : 'Обратная связь', 'url_name' : 'contact'},
        {'title' : 'Войти', 'url_name' : 'login'},
]

def index(request):
    posts = Women.objects.filter(is_published=True)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Главная страница',
        'cat_selected' : 0
    }

    return render(request, 'women/index.html', context)

def about(request):
    #posts = Women.objects.all()
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'women/about.html', context)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = AddPostForm()

    context = {
        'menu': menu,
        'form' : form,
        'title': 'Добавление статьи',
    }

    return render(request, 'women/addpage.html', context)

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id):
    return HttpResponse(f'Показываем статью с ID = { post_id }')

def show_category(request, cat_id):
    #return HttpResponse(f'Показываем категорию с ID = { cat_id }')
    posts = Women.objects.filter(cat_id = cat_id, is_published=True)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Отображение по рубрикам. Категория с id = ' + str(cat_id),
        'cat_selected' : cat_id
    }

    return render(request, 'women/index.html', context)



def pagenotfound404(request, exception):
    return HttpResponseNotFound('Страница не найдена')