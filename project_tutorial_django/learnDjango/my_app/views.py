from django.shortcuts import render, HttpResponse, redirect
from my_app.models import Article, Category
from my_app.forms import Article_forms
from django.db.models import Q

# Create your views here.
"""
    MVC = Modelo vista controlador. 
    MVT = Modelo Template vista.
   
    Con el segundo modelo la vista es el template y las
    acciones propias del controlador estan en la vista.
"""

def hello_world(request):
    return render(request, 'hello_world.html', {
        'text': '',
        'list': ['uno', 'dos', 'tres']
    })

def index(request):
    languages = ['JS', "C", "Java"]
    year = 2021
    lastyear = range(year, 2051)

    return render(request, 'index.html', {
        'variable': 'Dato desde la vista',
        'name': 'Lourdes',
        'languages': languages,
        'years': lastyear
    })

def contact(request, name=""):
    #return redirect('/index') usando url
    # return redirect('contacto', name='Lourdes') usando el nombre de la vista
    html = f"<h2>Contact {name}</h2>"

    return HttpResponse(html)

def create_article(request, title, content, public):
    article = Article(
        title = title,
        content = content,
        public = public,
    )
    article.save()
    return HttpResponse(f"Articulo creado: {article.title} - {article.content}")

def save_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        article = Article(
            title = title,
            content = content,
            public = public,
        )
        article.save()
    else:
        return HttpResponse("<h2> NO se ha podido gurdar el artículo </h2>")

    return render(request, 'create_article.html')

def create_forms_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):
    if request.method == 'POST':
        forms_completed = Article_forms(request.POST)

        if forms_completed.is_valid():
            data_form = forms_completed.cleaned_data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

        article = Article(
            title = title,
            content = content,
            public = public,
        )
        article.save()

        return redirect('articles')
    else:
        forms = Article_forms()
        return render(request, "create_full_article.html", {'forms': forms})

def article(request):
    try:
        article = Article.objects.get(pk=1) #id=1
        response = f"Articulo: {article.id}) {article.title} - {article.content}"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)

def edit_article(request, id):
    try:
        article = Article.objects.get(pk=id) #id=1
        article.title = "Batman"
        article.content = "Modificado el contenido"
        article.public = True

        article.save()
        response = f"Articulo: {article.id}) {article.title} - {article.content} se modificado correctamente"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)

def articles(request):
    '''
    articles_list = Article.objects.order_by('title') reverse order '-title'
    articles_list = Article.objects.order_by('title')(3:7) offset:limit
    '''

    '''
    lookups examples:
    articles_list = Article.objects.filter(title="Batman", id=8) --> AND
    articles_list = Article.objects.filter(id_lte=8) gt >, gte >=, lt <, lte <=
    articles_list = Article.objects.filter(title__contains="artículo")
    
    articles_list = Article.objects.filter(Q(title__contains="2") | Q(title__contains="3")) --> OR
    '''

    '''
    exlude examples:
    articles_list = Article.objects.filter(title="Batman").exclude(public=False)
    articles_list = Article.objects.filter(title="Batman", public=False)
    '''

    '''
    native querys:
    articles_list = Article.objects.raw("SELECT * FROM my_app.article WHERE title='Batman'")
    '''

    articles_list = Article.objects.all()
    print(articles_list)
    return render(request, 'articles.html', {
        'articles': articles_list
    })


def articles(request):
    articles_list = Article.objects.filter(public=True)
    return render(request, 'articles.html', {
        'articles': articles_list
    })

def delete_article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles')