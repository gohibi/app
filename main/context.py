from products.models import Category


def default():
    context ={}
    context['categories'] = Category.objects.all().order_by('-id')
    return context
