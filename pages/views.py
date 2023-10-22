from django.shortcuts import render


class HomePageView(render):
    template_name = "pages/home.html"

class AboutPageView(render):
    template_name = "pages/about.html"

class DetailPageView(render):
    template_name = "pages/detail.html"

class NewPageView(render):
    template_name = "pages/new.html"    