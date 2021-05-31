from django.db import models

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