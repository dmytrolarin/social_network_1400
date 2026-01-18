from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Profile(models.Model):
    about_me = models.TextField()
    phone_number = PhoneNumberField()
