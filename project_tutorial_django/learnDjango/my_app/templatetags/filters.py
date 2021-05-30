from django import template

register = template.Library()

@register.filter(name='regard')
def regard(value):
    long = ''
    if len(value) >= 8:
        long = '<p>Tu nombre es muy largo</p>'

    return f"<h1 style='background:green;color:white;'>Bienvenido, {value}</h1>" + long