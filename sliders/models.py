from django.db import models
from django.contrib.auth.models import User

class Slider(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='sliders/', blank=True, null=True)  # <-- new line

    def __str__(self):
        return self.name
