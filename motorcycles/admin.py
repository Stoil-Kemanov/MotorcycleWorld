from django.contrib import admin

from motorcycles.models import Motorcycle, MotorcycleParts, MotorcycleAccessories


# Register your models here.
@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    pass


@admin.register(MotorcycleParts)
class MotorcyclePartsAdmin(admin.ModelAdmin):
    pass


@admin.register(MotorcycleAccessories)
class MotorcycleAccessoriesAdmin(admin.ModelAdmin):
    pass
