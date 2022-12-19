from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    """
    Model that provides the fields to create/retrieve/update car postings
    in the db by the user instance.
    """
    brand_choices = [
        ("bmw", "Bmw"),
        ("mercedes-benz", "Mercedes-benz"),
        ("audi", "Audi"),
        ("volkswagen", "Volkswagen"),
        ("volvo", "Volvo"),
        ("ford", "Ford"),
        ("toyota", "Toyota"),
        ("honda", "Honda"),
        ("nissan", "Nissan"),
        ("mazda", "Mazda"),
        ("tesla", "Tesla"),
        ("renault", "Renault"),
        ("peugeot", "Peugeot"),
    ]

    gearbox_choices = [
        ("manual", "Manual"),
        ("automatic", "Automatic"),
    ]

    fueltype_choices = [
        ("petrol", "Petrol"),
        ("diesel", "Diesel"),
        ("electric", "Electric"),
        ("hybrid", "Hybrid"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    brand = models.CharField(
        max_length=32, choices=brand_choices
    )
    description = models.TextField()
    mileage = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    gearbox = models.CharField(
        max_length=32, choices=gearbox_choices, default='automatic'
    )
    fueltype = models.CharField(
        max_length=32, choices=fueltype_choices, default='petrol'
    )
    price = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_rb5ucj', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
