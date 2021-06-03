from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="título")
    content = RichTextField(max_length=500, verbose_name="contenido")
    slug = models.CharField(max_length=50, verbose_name="Slug", unique=True)
    order = models.IntegerField(default=0, verbose_name="Orden")
    public = models.BooleanField(verbose_name="publicado")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="creado en")
    update_at = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name= "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title