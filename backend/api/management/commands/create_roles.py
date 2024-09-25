from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from api.models import Profile


class Command(BaseCommand):
    help = "Create roles and assign permissions"

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        viewer_group, _ = Group.objects.get_or_create(name="Viewer")

        # Assign permissions (for example, on the Profile model)
        content_type = ContentType.objects.get_for_model(Profile)

        # Admin: all permissions
        permissions = Permission.objects.filter(content_type=content_type)
        admin_group.permissions.set(permissions)

        # Editor: add and change profile permissions
        editor_group.permissions.set(
            Permission.objects.filter(codename__in=["add_profile", "change_profile"])
        )

        # Viewer: only view permissions
        viewer_group.permissions.set(Permission.objects.filter(codename="view_profile"))

        self.stdout.write(self.style.SUCCESS("Roles created successfully!"))
