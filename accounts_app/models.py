from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    fathers_name = models.CharField(max_length=25)
    melicode = models.CharField(max_length=10)
    image = models.ImageField('profiles/images')


    def __str__(self):
        return self.user.username