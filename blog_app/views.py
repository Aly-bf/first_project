from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, 'blog_app/article_details.html', context={'article': article, "comments": comments})


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

