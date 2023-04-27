from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


@receiver(post_save, sender=get_user_model())
def add_to_default_group(sender, instance, created, **kwargs):
    if created:
        default_group = Group.objects.get(id=1)
        instance.groups.add(default_group)
