from django.shortcuts import render

def index(request):

    return render(request, 'main_app/index.html', {
        'title': 'Indice'
    })

def about_us(request):
    return render(request, 'main_app/about.html', {
        'title': 'Sobre nosotros:'
    })