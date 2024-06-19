from django import template
# from django.template.defaultfilters import urlencode
from django.utils.http import urlencode
from products.models import Category


register = template.Library()

@register.simple_tag()  
def category_tags():
    return Category.objects.all().order_by('id')


@register.simple_tag(takes_context=True)
def change_params(context,**kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)