from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Role(models.Model):
	role = models.CharField(max_length=30, primary_key=True)

	def __str__(self):
		return self.role

class Level(models.Model):
	level = models.CharField(max_length=10, primary_key=True)

	def __str__(self):
		return self.level

class Expression(models.Model):
	content = models.CharField(max_length=50, null=False, blank=False, unique=True)
	translation_it = models.CharField(max_length=50, null=True)
	note = models.CharField(max_length=300, null=True)
	context = models.CharField(max_length=30, null=True)
	example_en = models.CharField(max_length=150, null=True)
	example_it = models.CharField(max_length=150, null=True)
	is_phrasal_verb = models.BooleanField(default=False)
	is_formal = models.BooleanField(default=False)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	level = models.ForeignKey(Level, on_delete=models.CASCADE)


class User(AbstractUser):
	expression = models.ManyToManyField(Expression, through='Learn')


class Learn(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	expression = models.ForeignKey(Expression, on_delete=models.CASCADE)
	confidence = models.IntegerField(default=0)
