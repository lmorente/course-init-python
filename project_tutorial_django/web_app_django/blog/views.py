from django.shortcuts import render
from .models import Category, Article

# Create your views here.
def articles(request):
    articles = Article.objects.all()

    return  render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })