from django.db import models

from common.choices import ServicesType
from common.mixins import TimeStampMixin


class Service(TimeStampMixin, models.Model):
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30, choices=ServicesType)
    location = models.CharField(max_length=30)
    working_hours = models.CharField(max_length=50, help_text="e.g., Mon-Fri 9:00-17:00")
    phone = models.CharField(max_length=30)
    email = models.EmailField()


    class Meta:
        ordering = ['-created_at']
