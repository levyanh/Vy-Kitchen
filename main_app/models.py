from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

# Recipe model
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredient = models.TextField(max_length=1000)
    instruction = models.TextField(max_length=3000)
    image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']