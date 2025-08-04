from django.contrib import admin

from clothing.models import Clothing


# Register your models here.
@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('make', 'model')
    search_help_text = 'Search by make/model'
    ordering = ('-price',)
    list_per_page = 15
