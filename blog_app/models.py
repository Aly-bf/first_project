from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django. urls import reverse
from django.utils.text import slugify

# manytoOne
# manytoMany
# OnetoOne

class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Article(models.Model):
    auther = models.ForeignKey(User, models.CASCADE, )
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/article')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True, blank=True)


    # class Meta:
    #     ordering = ('-updated','-created') baraye taiqr tartib
        # verbose_name = taqir esm class Article
        #  verbose_name_plural = taqir esm jam koli dakhel admin


    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.slug = slugify(self.title)
        super(Article, self).save()


    def get_absolute_url(self):
        return reverse('blog_app:detail', args=[self.slug])
    # or kwargs= 'pk': self.id

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'



# class Detail(models.Model):
#     auther = models.ForeignKey(User, models.CASCADE)
#     title = models.CharField(max_length=20)
#     body = models.TextField()
#     image = models.ImageField(upload_to='images/detail')
#     created = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)