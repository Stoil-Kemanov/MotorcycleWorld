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


class EngineType(models.TextChoices):
    INLINE = 'Inline', 'Inline'
    V_ENGINE = 'V', 'V'
    OTHER = 'Other', 'Other'


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
    CLOTHING = 'Clothing', 'Clothing'


class ClothingType(models.TextChoices):
    JACKET = 'Jacket', 'Jacket'
    PANTS = 'Pants', 'Pants'
    HELMET = 'Helmet', 'Helmet'


class ServicesType(models.TextChoices):
    ELECTRIC = 'Electric', 'Electric'
    MECHANICAL = 'Mechanical', 'Mechanical'
    PAINTING = 'Painting', 'Painting'