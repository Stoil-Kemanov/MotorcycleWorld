from django.contrib import admin

from motorcycles.models import Motorcycle


# Register your models here.
@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    pass
