from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from .forms import LoginForm, SignupForm

from .models import Role, Level, Expression, Learn, User
from random import choice

import json


def redir_home(request):
    return redirect('vocapp:home')

def adjust_confidence(request, expression_id):
	# if there is a user logged in
	# get the curret confidence of the user with the "expression_id" word
	# if the guessing value is 1 the increase it
	# else decrease it 
	
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)
		expr = Expression.objects.get(pk = expression_id)
		try:
			association = Learn.objects.get(user = user, expression = expr)
			if (request.POST["guessing"] == '1'):	# guessed
				association.confidence += 1
			elif (request.POST["guessing"] == '0'):	# not guessed
				association.confidence -= 1
				if (association.confidence < 0):
					association.confidence = 0
			association.save()
		except Learn.DoesNotExist:	# create a new association between user and expression
			new_association = Learn(user = user, expression = expr, confidence=0)
			new_association.save()

	# if there is no user logged in just redirect to home
	return redirect('vocapp:home')

def home(request):
    # update this two list only once (maybe by a refresh button)
	all_ids = Expression.objects.values_list('id', flat = True)
	levels = Level.objects.values_list('level', flat = True)
    
	expression_data = Expression.objects.get(pk = choice(all_ids))	# pick a random expression
	context = {
		"levels": levels,
		"expression_info": expression_data,
		"User" : "username",
	}
	
	return render(request, "vocapp/home.html", context)

def search(request):
	expressions_list = dict(Expression.objects.values_list('id', 'content'))
	context = {
		"expressions_list" : json.dumps(expressions_list),
    }
	return render(request, "vocapp/search.html", context)


def inspect_expression(request, expression_id):
	expression_info = Expression.objects.get(pk = expression_id)
	context = {
		"expression_id" : expression_id,
		"expression_info": expression_info,
	}
	return render(request, "vocapp/expression.html", context)


def dashboard(request):
	# check if user is autenticated, if not redirect to home
	if request.user.is_authenticated:
		context = {
			"not_learned" : 123,
			"learning" : 789,
			"learned" : 456,
		}
		return render(request, "vocapp/dashboard.html", context)
	else:
		return redirect("vocapp:login_user")

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("vocapp:login_user")
	else:
		form = SignupForm()
	return render(request, "vocapp/signup.html", {'form': form})

def login_user(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				return redirect("vocapp:home")
	else:
		form = LoginForm()
	return render(request, "vocapp/login.html", {'form': form})
	

def logout_user(request):
    logout(request)
    return redirect("vocapp:login_user")