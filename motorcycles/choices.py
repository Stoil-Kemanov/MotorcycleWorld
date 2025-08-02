from django.db import models


class MotorcycleType(models.TextChoices):
    SPORT = 'Sport', 'Sport'
    TOURING = 'Touring', 'Touring'
    CRUISER = 'Cruiser', 'Cruiser'
    OFF_ROAD = 'Off-Road', 'Off-Road'
    OTHER = 'Other', 'Other'


class MotorcyclePartsCategory(models.TextChoices):
    ENGINE = 'Engine', 'Engine'
    CHAIN_DRIVE = 'Chain Drive', 'Chain Drive'
    SUSPENSION = 'Suspension', 'Suspension'
    BRAKES = 'Brakes', 'Brakes'
    EXHAUST = 'Exhaust', 'Exhaust'
    ELECTRIC = 'Electric', 'Electric'
    FAIRINGS = 'Fairings', 'Fairings'
    TYRES = 'Tyres', 'Tyres'
    OTHER = 'Other', 'Other'


class CategorySearch(models.TextChoices):
    ALL = 'All', 'All'
    MOTORCYCLES = 'Motorcycles', 'Motorcycles'
    PARTS = 'Parts', 'Parts'
    ACCESSORIES = 'Accessories', 'Accessories'
