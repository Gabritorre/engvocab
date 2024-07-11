from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Role, Level, Expression, User

from django.forms import TextInput, Textarea
from django.db import models

admin.site.site_header = "Engvocab Admin page"
admin.site.site_title = "Engvocab"

class UserAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["username", "is_staff"]
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]
    
    search_fields = ["username"]
    ordering = ["username"]
    filter_horizontal = []


class ExpressionAdmin(admin.ModelAdmin):
	list_display = ["id", "content", "translation_it", "level", "is_phrasal_verb"]
	search_fields = ["content", "translation_it"]
	ordering = ["content", "translation_it", "level"]

	def get_form(self, request, obj=None, **kwargs):
		form = super(ExpressionAdmin, self).get_form(request, obj, **kwargs)
		form.base_fields['note'].widget.attrs['style'] = 'width: 60em;'
		form.base_fields['example_en'].widget.attrs['style'] = 'width: 60em;'
		form.base_fields['example_it'].widget.attrs['style'] = 'width: 60em;'
		return form



admin.site.register(Role)
admin.site.register(Level)
admin.site.register(Expression, ExpressionAdmin)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)