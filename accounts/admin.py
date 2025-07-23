from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import MotoUser, Profile


# Register your models here.
@admin.register(MotoUser)
class MotoUserAdmin(UserAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
