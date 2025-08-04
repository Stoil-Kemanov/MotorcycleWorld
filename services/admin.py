from django.contrib import admin

from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'location', 'working_hours', 'phone', 'email')
    search_fields = ('specialization', 'location')
    search_help_text = 'Search by specialization or location'
