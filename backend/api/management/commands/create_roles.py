from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from api.models import Profile  # Import your Profile model

class Command(BaseCommand):
    help = 'Create roles (Admin, Editor, Viewer) and assign permissions to them'

    def handle(self, *args, **kwargs):
        # Create the Admin, Editor, and Viewer groups
        admin_group, created = Group.objects.get_or_create(name='Admin')
        editor_group, created = Group.objects.get_or_create(name='Editor')
        viewer_group, created = Group.objects.get_or_create(name='Viewer')

        # Get the content type for the Profile model
        content_type = ContentType.objects.get_for_model(Profile)

        # Admin:
