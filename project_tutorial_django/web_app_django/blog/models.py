from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    descripction = models.CharField(max_length=500, verbose_name="descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
    def __str__(self):
        return self.name

class Article(models.Model):
        title = models.CharField(max_length=100, verbose_name="titulo")
        content = RichTextField(max_length=500, verbose_name="contenido")
        image = models.ImageField(default='null', verbose_name="imagen", upload_to="articles")
        public = models.BooleanField(default=False, verbose_name="publicado")
        user = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE, editable=False)
        categories = models.ManyToManyField(Category, blank=True)
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
        update_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

        class Meta:
            verbose_name = 'Artículo'
            verbose_name_plural = 'Artículos'

        def __str__(self):
            return self.title