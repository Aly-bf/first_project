from blog_app.models import Article, Category

def recent_article(request):
    recent_article = Article.objects.order_by('-created')
    categories = Category.objects.all()
    return {'recent': recent_article, 'categories': categories}