from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import MotoUser, Profile


@receiver(post_save, sender=MotoUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
