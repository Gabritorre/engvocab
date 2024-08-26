from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxLengthValidator


class Role(models.Model):
	role = models.CharField(max_length=30, primary_key=True)

	def __str__(self):
		return self.role


class Level(models.Model):
	level = models.CharField(max_length=10, primary_key=True)

	def __str__(self):
		return self.level


class Expression(models.Model):
	content = models.CharField(max_length=75, null=False, blank=False, unique=True)
	translation_it = models.CharField(max_length=100, null=True)
	note = models.CharField(max_length=350, null=True)
	context = models.CharField(max_length=100, null=True)
	example_en = models.CharField(max_length=200, null=True)
	example_it = models.CharField(max_length=200, null=True)
	is_phrasal_verb = models.BooleanField(default=False)
	is_formal = models.BooleanField(default=False)
	is_figurative = models.BooleanField(default=False)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	level = models.ForeignKey(Level, on_delete=models.CASCADE)

	def __str__(self):
		return self.content


class User(AbstractUser):
	expression = models.ManyToManyField(Expression, through='Learn')


class Learn(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	expression = models.ForeignKey(Expression, on_delete=models.CASCADE)
	confidence = models.IntegerField(default=0)


class Report(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	expression = models.ForeignKey(Expression, on_delete=models.CASCADE)
	fields = models.CharField(max_length=100, null=False, blank=False)
	message = models.TextField(max_length=350, blank=True, validators=[MaxLengthValidator(350)])
	created_at = models.DateTimeField(auto_now_add=True)