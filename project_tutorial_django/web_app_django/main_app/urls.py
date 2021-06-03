from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name="index"),
    path('about-us/', views.about_us, name="about_us"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]
