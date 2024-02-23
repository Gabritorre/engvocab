from django.db import models

# Create your models here.
class Roles(models.Model):
	role = models.CharField(max_length=30, primary_key=True)


class Levels(models.Model):
	level = models.CharField(max_length=10, primary_key=True)

class Expressions(models.Model):
	id = models.IntegerField(primary_key=True)
	content = models.CharField(max_length=50)
	translation_it = models.CharField(max_length=50)
	note = models.CharField(max_length=300)
	context = models.CharField(max_length=30)
	example_en = models.CharField(max_length=150)
	example_it = models.CharField(max_length=150)
	is_phrasal_verb = models.BooleanField()
	is_formal = models.BooleanField()
	role = models.ForeignKey(Roles, on_delete=models.CASCADE)
	level = models.ForeignKey(Levels, on_delete=models.CASCADE)

class Users(models.Model):
	username = models.CharField(max_length=30, primary_key=True)
	password = models.CharField(max_length=100)
	last_connection = models.DateTimeField()


class Learn(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	expression = models.ForeignKey(Expressions, on_delete=models.CASCADE)
	confidence = models.IntegerField()



