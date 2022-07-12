from django.shortcuts import render
from django import forms

def index(request):
    return render(request, "gymDirectory/index.html", {})

def about(request):
    return render(request, "gymDirectory/about.html", {})

def contact(request):
    return render(request, "gymDirectory/contact.html", {})

def gallery(request):
    return render(request, "gymDirectory/gallery.html", {})

def pricing(request):
    return render(request, "gymDirectory/pricing.html", {})

def services(request):
    return render(request, "gymDirectory/services.html", {})