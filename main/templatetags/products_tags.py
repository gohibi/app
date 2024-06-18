from django import template
from django.template.defaultfilters import urlencode
from products.models import Category


register = template.Library()

@register.simple_tag()  
def category_tags():
    context ={}
    context['categories'] = Category.objects.all().order_by('-id')
    return context

@register.simple_tag(takes_context=True)
def change_params(context,**kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)