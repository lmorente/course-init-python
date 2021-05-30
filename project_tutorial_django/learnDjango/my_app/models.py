from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    images = models.ImageField(default='null', upload_to='articles')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True) #Add first time
    update_at = models.DateTimeField(auto_now=True) ##Add always

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

