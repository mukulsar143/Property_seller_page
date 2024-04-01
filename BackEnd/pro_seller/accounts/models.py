from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import *


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique = True, max_length=254)
    is_varified = models.BooleanField(default = False)
    role_choices = [
        ('property_owner', 'Property Owner'),
        ('buyer', 'Buyer'),
    ]
    role = models.CharField(max_length = 20, choices=role_choices, null = True)
    mobile = models.CharField(max_length=15)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def name(self):
        return self.first_name + '' + self.last_name
            
    
    def __str__(self):
        return self.email
    
