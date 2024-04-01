from django.db import models
from accounts.models import User


class Property(models.Model):
    owner = models.ForeignKey(User, related_name='owned_properties',null = True, blank = True, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    rooms = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('available', 'Available'),
        ('sold_out', 'Sold Out'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)

    def __str__(self):
        return f"Property in {self.location}, Owner: {self.owner}"