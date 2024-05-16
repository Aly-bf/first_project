from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog_app/article_details.html', context={'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    pageinator = Paginator(articles, 1)
    objects_list = pageinator.get_page(page_number)

    return render(request, 'blog_app/article_list.html', context={'articles': objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'blog_app/article_list.html', context={'articles': articles}) 

def comments(request):
        article_comments = Comment.comments.all()
        return render(request, 'blog_app/article_details.html', context={'article_comments': article_comments})