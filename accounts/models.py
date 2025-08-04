from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.validators import PhoneNumberValidator
from common.choices import BodyType, RidingStyle, ExperienceLevel, EngineType


class MotoUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)


class Profile(models.Model):

    # Profile instances are automatically created via post_save signal when a MotoUser is created.

    user = models.OneToOneField(MotoUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(
        unique=True, max_length=15, blank=True, null=True, validators=[
            PhoneNumberValidator()
        ],
        error_messages={'unique': "That phone number is already in use!"},
        help_text="Enter your phone number (digits, spaces, hyphens, and parentheses allowed)")
    date_of_birth = models.DateField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Height in centimeters")
    weight = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Weight in kilograms")
    body_type = models.CharField(max_length=10, choices=BodyType, blank=True, null=True)
    riding_style = models.CharField(max_length=10, choices=RidingStyle, blank=True, null=True)
    experience = models.CharField(max_length=30, choices=ExperienceLevel, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username


class OwnedMotorcycle(models.Model):
    user = models.ForeignKey(MotoUser, on_delete=models.CASCADE, related_name='owned_motorcycle')
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    production_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2025)])
    engine_type = models.CharField(max_length=20, choices=EngineType)
    engine_volume = models.PositiveSmallIntegerField()
    engine_power = models.PositiveSmallIntegerField()
