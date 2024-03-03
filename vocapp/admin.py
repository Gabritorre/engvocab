from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Role, Level, Expression, User

# Register your models here.

admin.site.register(Role)
admin.site.register(Level)
admin.site.register(Expression)
admin.site.register(User, UserAdmin)