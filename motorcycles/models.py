from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.choices import EngineType


# Create your models here.
class Motorcycle(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    production_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2025)])
    engine_type = models.CharField(max_length=20, choices=EngineType)
    engine_volume = models.PositiveSmallIntegerField(blank=True, null=True)
    engine_power = models.PositiveSmallIntegerField(blank=True, null=True)
