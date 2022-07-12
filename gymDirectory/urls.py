from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.about, name="about"),
    path("contact-us", views.contact, name="contact"),
    path("gallery", views.gallery, name="gallery"),
    path("pricing", views.pricing, name="pricing"),
    path("services", views.services, name="services"),
    path("login", RedirectView.as_view(url='/accounts/login_user', permanent=True), name = "login"),
]