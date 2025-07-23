from django.db import models


class BodyType(models.TextChoices):
    SLIM = 'Slim', 'Slim'
    ATHLETIC = 'Athletic', 'Athletic'
    CHUBBY = 'Chubby', 'Chubby'


class RidingStyle(models.TextChoices):
    SPORT = 'Sport', 'Sport'
    TOURING = 'Touring', 'Touring'
    CRUISER = 'Cruiser', 'Cruiser'
    OFF_ROAD = 'Off-Road', 'Off-Road'


class ExperienceLevel(models.TextChoices):
    BEGINNER = 'Beginner (0-1 years)', 'Beginner (0-1 years)'
    INTERMEDIATE = 'Intermediate (2-5 years)', 'Intermediate (2-5 years)'
    ADVANCED = 'Advanced (5+ years)', 'Advanced (5+ years)'
