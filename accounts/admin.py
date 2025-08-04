from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import MotoUser, Profile, OwnedMotorcycle


# Register your models here.
@admin.register(MotoUser)
class MotoUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('username', 'email')
    search_help_text = 'Search by username or email'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_email', 'phone_number')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    search_help_text = 'Search by first name or last name'
    ordering = ('first_name',)

    @staticmethod
    def user_email(obj):
        return obj.user.email


@admin.register(OwnedMotorcycle)
class OwnedMotorcycleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'production_year', 'user_email')
    list_filter = ('make', 'model', 'production_year')
    search_fields = ('make', 'model', 'production_year')
    search_help_text = 'Search by make/model or production year'
    ordering = ('production_year',)

    @staticmethod
    def user_email(obj):
        return obj.user.email
