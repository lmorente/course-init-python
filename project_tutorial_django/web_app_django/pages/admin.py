from django.contrib import admin
from pages.models import Page

# Register your models here.
admin.site.register(Page)
title = "Panel de administración"
subtitle = "Menu"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle

