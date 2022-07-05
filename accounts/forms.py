from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Customer, Staff, User

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    membership_tier = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.email_address = self.cleaned_data.get('email_address')
        customer.membership_tier = self.cleaned_data.get('membership_tier')
        customer.save()
        return user

class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    role = forms.CharField(required=True)
    employeeID = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(user=user)
        staff.role = self.cleaned_data.get('role')
        staff.employeeID = self.cleaned_data.get('employeeID')
        staff.save()
        return user
