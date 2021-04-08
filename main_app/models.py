from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avarta = models.ImageField(default='default_avarta.jpg',upload_to='user_avarta')

    def __str__(self):
        return self.user.username
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="recipe_images")
    ingredient = models.TextField(max_length=2000)
    instruction = models.TextField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_date']

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.user)
