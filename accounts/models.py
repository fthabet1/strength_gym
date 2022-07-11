from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

class Customer(models.Model):

    member_tiers = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )

    username = models.CharField(User, max_length = 50, primary_key=True)
    email_address = models.EmailField(max_length=30)
    membership_tier = models.CharField(max_length = 1, choices = member_tiers)

class Staff(models.Model):

    employee_roles = (
        ('F', 'Front Desk'),
        ('C', 'Cleaner'),
        ('P', 'Personal Trainer'),
        ('M', 'Management')
    )
    username = models.CharField(User, max_length = 50, primary_key=True)
    role = models.CharField(max_length = 1, choices = employee_roles)
    employeeID = models.IntegerField()
