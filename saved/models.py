from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Save(models.Model):
    """
    Model to save a car ad. 'owner' is a User instance
    and 'car' is a Car instance. 'unique_together' prevent
    a user from saving the same car ad more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='saved')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'car']

    def __str__(self):
        return f'{self.owner} {self.car}'
