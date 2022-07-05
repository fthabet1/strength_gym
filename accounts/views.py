from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .forms import CustomerSignUpForm, StaffSignUpForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    return render(request, 'accounts/register.html')

class customer_register(CreateView):
    model = User  
    form_class = CustomerSignUpForm
    template_name= 'accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

class staff_register(CreateView):
    model = User  
    form_class = StaffSignUpForm
    template_name= 'accounts/staff_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/accounts/home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login.html',context={
        'form':AuthenticationForm()
        })

def logout_user(request):
    logout(request)
    return redirect('/accounts/home')