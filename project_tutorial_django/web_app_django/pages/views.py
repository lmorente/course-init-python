from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Page

# Create your views here.
@login_required(login_url="login")
def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, "pages/page.html", {
                  "title": page.title,
                  "date": page.create_at,
                  "content": page.content
    })
