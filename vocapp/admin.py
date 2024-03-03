from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Role, Level, Expression, User

class UserAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["username", "password", "is_staff"]
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]
    
    search_fields = ["username"]
    ordering = ["username"]
    filter_horizontal = []


admin.site.register(Role)
admin.site.register(Level)
admin.site.register(Expression)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)