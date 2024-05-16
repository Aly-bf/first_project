from django.shortcuts import render, redirect
from blog_app.models import Article
from django.urls import reverse



def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-created', '-updated')[:3]
    return render(request, 'home_app/index.html', context={'articles': articles, 'recent_articles': recent_articles, 'name': 'codeyad'})



def sidebar(request):
    context = {'name': 'alybehroozifar'}
    return render(request, 'includes/sidebar.html', context)