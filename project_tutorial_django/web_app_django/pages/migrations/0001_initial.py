# Generated by Django 3.0.5 on 2021-05-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('content', models.TextField(max_length=500, verbose_name='contenido')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='Slug')),
                ('public', models.BooleanField(verbose_name='publicado')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='creado en')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='actualizado en')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
            },
        ),
    ]
