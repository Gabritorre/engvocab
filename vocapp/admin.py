from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Role, Level, Expression, User, Learn


admin.site.site_header = "Engvocab Admin page"
admin.site.site_title = "Engvocab"

class UserAdmin(UserAdmin):
	list_display = ["username", "is_staff", "date_joined", "last_login"]
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
		form.base_fields['content'].widget.attrs['style'] = 'width: 25em;'
		form.base_fields['translation_it'].widget.attrs['style'] = 'width: 25em;'
		form.base_fields['context'].widget.attrs['style'] = 'width: 25em;'
		form.base_fields['note'].widget.attrs['style'] = 'width: 70em;'
		form.base_fields['example_en'].widget.attrs['style'] = 'width: 70em;'
		form.base_fields['example_it'].widget.attrs['style'] = 'width: 70em;'
		form.base_fields['role'].widget.attrs['style'] = 'width: 10em;'
		form.base_fields['level'].widget.attrs['style'] = 'width: 10em;'
		return form

class LearnAdmin(admin.ModelAdmin):
	list_display = ["user", "expression", "confidence"]
	search_fields = ["user", "expression"]
	ordering = ["user", "expression"]


admin.site.register(Role)
admin.site.register(Level)
admin.site.register(Expression, ExpressionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Learn, LearnAdmin)

admin.site.unregister(Group)