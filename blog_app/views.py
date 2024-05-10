from django.shortcuts import render, get_object_or_404
from .models import Article


def post_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, 'blog_app/article_details.html', context={'article': article})