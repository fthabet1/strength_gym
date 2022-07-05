from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

class Customer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email_address = models.EmailField(max_length=30)
    membership_tier = models.CharField(max_length=30)

class Staff(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=30)
    employeeID = models.IntegerField()
