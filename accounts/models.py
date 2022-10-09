
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    bio = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(update_to='accounts/covers/%Y/%m/%d/', blank=True, default='')
