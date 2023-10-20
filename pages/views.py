from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class DetailPageView(TemplateView):
    template_name = "pages/detail.html"

class NewPageView(TemplateView):
    template_name = "pages/new.html"    