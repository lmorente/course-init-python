from django.shortcuts import render
from .models import Page

# Create your views here.
def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, "pages/page.html", {
                  "title": page.title,
                  "date": page.create_at,
                  "content": page.content
    })
