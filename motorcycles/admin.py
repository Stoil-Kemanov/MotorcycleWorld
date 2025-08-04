from django.contrib import admin

from motorcycles.models import Motorcycle, MotorcycleParts, MotorcycleAccessories


# Register your models here.
@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'production_year', 'type', 'price')
    list_filter = ('type',)
    search_fields = ('make', 'model')
    search_help_text = 'Search by make/model'
    ordering = ('-production_year',)
    list_per_page = 10

@admin.register(MotorcycleParts)
class MotorcyclePartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'price', 'get_compatible_motorcycles', 'description')
    search_fields = ('name', 'make')
    search_help_text = 'Search by name/make'
    ordering = ('-price',)
    list_per_page = 20

    @admin.display(description="Compatible Motorcycles")
    def get_compatible_motorcycles(self, obj: MotorcycleParts):
        return ', '.join(str(m) for m in obj.compatible_motorcycles.all())

@admin.register(MotorcycleAccessories)
class MotorcycleAccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'price', 'description')
    search_fields = ('name', 'make')
    search_help_text = 'Search by name/make'
    ordering = ('-price',)
    list_per_page = 20
