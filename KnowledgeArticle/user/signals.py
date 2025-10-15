from django.contrib.auth.models import User, Permission, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender = User)
def add_groups(sender, instance, created, **kwargs):
    if not created:
        return

    group_name = None

    if instance.is_superuser:
        group_name = 'Admin'

    elif instance.is_staff and not instance.is_superuser:
        group_name = 'Editor'

    elif instance.is_active and not instance.is_staff:
        group_name = 'Viewer'

    if not group_name:
        return

    group, _ = Group.objects.get_or_create(name=group_name)
    permission_codenames = settings.USER_GROUP_PERMISSIONS.get(group_name, [])

    permissions = Permission.objects.filter(codename__in = permission_codenames)

    for perm in permissions:
        if not group.permissions.filter(id=perm.id).exists():
            group.permissions.add(perm)

    instance.groups.add(group)