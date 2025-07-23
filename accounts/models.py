from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.choices import BodyType, RidingStyle, ExperienceLevel


class MotoUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(MotoUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Height in centimeters")
    weight = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Weight in kilograms")
    body_type = models.CharField(max_length=10, choices=BodyType, blank=True, null=True)
    riding_style = models.CharField(max_length=10, choices=RidingStyle, blank=True, null=True)
    experience = models.CharField(max_length=30, choices=ExperienceLevel, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
