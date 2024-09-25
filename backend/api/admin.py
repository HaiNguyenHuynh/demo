from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import GroupAdmin
from .models import Profile


# Inline profile with User in admin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]


# Unregister and re-register User with new inline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

if admin.site.is_registered(Group):
    admin.site.unregister(Group)

# Then register it again (if needed)
admin.site.register(Group, GroupAdmin)
