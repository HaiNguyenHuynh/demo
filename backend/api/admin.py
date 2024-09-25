from django.contrib import admin
from django.contrib.auth.models import User, Group
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

# Register groups for role management
# admin.site.register(Group)
