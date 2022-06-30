from django.shortcuts import render

def index(request):
    return render(request, "gymDirectory/index.html", {})

def about(request):
    return render(request, "gymDirectory/about.html", {})