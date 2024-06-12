from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Category

# Create your views here.

class indexView(TemplateView):
    template_name = "base/index.html"
    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['content'] = "Magasin"
        context['title'] = "Mon Magasin"
        return context

class AboutView(TemplateView):
    template_name = "base/about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['content'] = "Magasin"
        context['title'] = "Mon Magasin"
        context['about_us'] ="Lorem ipsum dolor sit amet consectetur adipisicing elit."
        return context