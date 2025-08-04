from django.core.validators import MinValueValidator
from django.db import models

from common.choices import ClothingType, BodyType, RidingStyle
from common.mixins import TimeStampMixin


class Clothing(TimeStampMixin, models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=ClothingType)
    fit = models.CharField(max_length=20, choices=BodyType, blank=True)
    style = models.CharField(max_length=20, choices=RidingStyle)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.make} {self.model} {self.category}'
