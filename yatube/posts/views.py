from django.shortcuts import render
from .models import Post

def index(request):
    title = 'Главная страница проекта "Yatube"'
    posts =  Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта "Yatube"'
    context = {
        'text': title,
    }
    return render(request, template, context)