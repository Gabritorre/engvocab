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
    
	# if there is no user logged in just redirect to home
    print("id: ", expression_id)
    print("value: ", request.POST["guessing"])
    return redirect('vocapp:home')

def home(request):
    # update this two list only once (maybe by a refresh button)
	all_ids = Expression.objects.values_list('id', flat = True)
	levels = Level.objects.values_list('level', flat = True)
    
	expression_data = Expression.objects.get(pk = choice(all_ids))
	context = {
		"levels": levels,
		"expression_info": expression_data,
		"User" : "username",
	}
	
	return render(request, "vocapp/home.html", context)

def search(request):
	expressions_list = dict(Expression.objects.values_list('id', 'content'))
	context = {
		"User" : "username",
		"expressions_list" : json.dumps(expressions_list),
    }
	return render(request, "vocapp/search.html", context)


def inspect_expression(request, expression_id):
	expression_info = Expression.objects.get(pk = expression_id)
	context = {
		"expression_id" : expression_id,
		"expression_info": expression_info,
		"User" : "username",
	}
	return render(request, "vocapp/expression.html", context)


def dashboard(request):
    context = {
        "not_learned" : 123,
        "learning" : 789,
        "learned" : 456,
        "User" : "username",
    }
    return render(request, "vocapp/dashboard.html", context)

def signin(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("vocapp:login")
	else:
		form = SignupForm()
	return render(request, "vocapp/signin.html", {'form': form})

def login(request):
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
	

def logout(request):
    logout(request)
    return redirect("vocapp:login")