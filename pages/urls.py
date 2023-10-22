from django.urls import path
from .views import HomePageView, AboutPageView, NewPageView, DetailPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("new/", NewPageView.as_view(), name="new"),
    path("detail/", DetailPageView.as_view(), name="detail"),
]