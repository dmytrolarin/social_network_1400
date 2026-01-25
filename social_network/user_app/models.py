from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    about_me = models.TextField()
    phone_number = PhoneNumberField()
    avatar = models.ImageField(upload_to='images/avatars/', null=True)
    
    # def __str__(self):
    #     return self.user

    
