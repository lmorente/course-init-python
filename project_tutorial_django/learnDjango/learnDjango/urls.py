"""learnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
#App
import my_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', my_app.views.index, name='index_url'),
    path('hello-world/', my_app.views.hello_world, name='hello_world_url'),
    path('contact/<str:name>', my_app.views.contact, name='contact'),
    path('contact/', my_app.views.contact, name='contact_url'),
    path('article/create/<str:title>/<str:content>/<str:public>', my_app.views.create_article, name='create_article'),
    path('article', my_app.views.article, name='article'),
    path('article/edit/<int:id>', my_app.views.edit_article, name='edit_article'),
    path('articles', my_app.views.articles, name='articles'),
    path('article/forms-create', my_app.views.create_forms_article, name='article-forms'),
    path('article/forms-full-create', my_app.views.create_full_article, name='create_full_article'),
    path('article/save', my_app.views.save_article, name='save'),
    path('article/delete/<int:id>', my_app.views.delete_article, name='delete_article'),
]

#Panel config
admin.site.site_header = "Curso web python"
admin.site.site_title = "Django"
admin.site.index_title = "Panel de gestión"

#Images config
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)