from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path('return', RedirectView.as_view(url='/strength_gym/', permanent=True)),
    path("customer_register", views.customer_register.as_view(), name = "customer_register"),
    path("staff_register", views.staff_register.as_view(), name="staff_register"),
]