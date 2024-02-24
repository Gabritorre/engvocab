from django.db import models

# Create your models here.
class Roles(models.Model):
	role = models.CharField(max_length=30, primary_key=True)


class Levels(models.Model):
	level = models.CharField(max_length=10, primary_key=True)

class Expressions(models.Model):
	content = models.CharField(max_length=50, null=False, blank=False, unique=True)
	translation_it = models.CharField(max_length=50, null=True)
	note = models.CharField(max_length=300, null=True)
	context = models.CharField(max_length=30, null=True)
	example_en = models.CharField(max_length=150, null=True)
	example_it = models.CharField(max_length=150, null=True)
	is_phrasal_verb = models.BooleanField(default=False)
	is_formal = models.BooleanField(default=False)
	role = models.ForeignKey(Roles, on_delete=models.CASCADE)
	level = models.ForeignKey(Levels, on_delete=models.CASCADE)

class Users(models.Model):
	username = models.CharField(max_length=30, primary_key=True)
	password = models.CharField(max_length=100, null=False, blank=False)
	expression = models.ManyToManyField(Expressions, through='Learn')
	last_connection = models.DateTimeField("last connection")


class Learn(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	expression = models.ForeignKey(Expressions, on_delete=models.CASCADE)
	confidence = models.IntegerField(default=0)
