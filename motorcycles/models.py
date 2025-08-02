from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.choices import EngineType
from motorcycles.choices import MotorcycleType, MotorcyclePartsCategory


class Motorcycle(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    production_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2025)])
    type = models.CharField(max_length=10, choices=MotorcycleType, default=MotorcycleType.OTHER)
    engine_type = models.CharField(max_length=20, choices=EngineType, default=EngineType.OTHER)
    engine_volume = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(2200)])
    engine_power = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.make} {self.model} {self.production_year}'


class MotorcycleParts(models.Model):
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=MotorcyclePartsCategory, default=MotorcyclePartsCategory.OTHER)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00)
    compatible_motorcycles = models.ManyToManyField(Motorcycle, blank=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.make}'

    class Meta:
        verbose_name_plural = 'Motorcycle Parts'


class MotorcycleAccessories(models.Model):
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.make}'

    class Meta:
        verbose_name_plural = 'Motorcycle Accessories'
