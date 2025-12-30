from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=20, default="male")
    contact_number = models.CharField(max_length=20,blank=True, default="")
    zip_code = models.CharField(max_length=20,blank=True, default="")
    role = models.CharField(max_length=40, default="user")
    subscription_type = models.CharField(max_length=40, default="free")
    birth_date = models.DateField(blank=True, null=True)  
    image = models.ImageField(upload_to='profiles/', blank=True, null=True) 


    def __str__(self):
        return f"{self.user.username}'s Profile"

