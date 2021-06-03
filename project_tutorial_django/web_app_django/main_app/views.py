from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def index(request):

    return render(request, 'main_app/index.html', {
        'title': 'Indice'
    })

@login_required(login_url="login")
def about_us(request):
    return render(request, 'main_app/about.html', {
        'title': 'Sobre nosotros'
    })

def register_page(request):
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')
            return redirect('index')


    return render(request,'users/register.html', {
        'title' : 'Resgistro',
        'register_form': register_form
    })

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'No te has idenficado correctamente')
    return render(request, 'users/login.html',{
        'title' : 'Login',
    })

def logout_user(request):
    logout(request)
    return redirect('login')
