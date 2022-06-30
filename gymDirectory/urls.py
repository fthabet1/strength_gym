from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/about", views.about, name="about"),
    path("/contact", views.contact, name="contact"),
    path("/portfolio", views.portfolio, name="portfolio"),
    path("/pricing", views.pricing, name="pricing"),
    path("/services", views.services, name="services"),
]