from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.db.models import 
# models.py


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        # Get the group that corresponds to the user's department
        group = Group.objects.get(name=instance.department)

        # Add the user to the group
        group.user_set.add(instance)