from django.db import models

class Flight(models.Model):
    FLIGHT_TYPES = [
        ('NAC', 'Nacional'),
        ('INT', 'International'),
    ]

    name = models.CharField(max_length=100)
    flightType= models.CharField(max_length=15, choices=FLIGHT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name