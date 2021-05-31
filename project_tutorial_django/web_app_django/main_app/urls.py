from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name="index"),
    path('about-us/', views.about_us, name="about_us")
]
