from django.shortcuts import render, redirect
from blog_app.models import Article
from django.urls import reverse


def home(request):
    articles = Article.objects.all()
    return render(request, 'home_app/index.html', context={'articles': articles})