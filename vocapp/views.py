from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Role, Level, Expression, User, Learn
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
	expressions_list = list(Expression.objects.values_list('content', flat = True))
	context = {
		"User" : "username",
		"expressions_list" : json.dumps(expressions_list),
    }
	return render(request, "vocapp/search.html", context)

def find_expression(request):
    # if expression found redirect to inspect_expression with expression_id.
    # If not found redirect to search with error message.
    expression_name = request.GET["expression_name"]
    expression_id = 0
    return HttpResponseRedirect(reverse("vocapp:inspect_expression", args=(expression_id,)))

def inspect_expression(request, expression_id):
    context = {
        "expression_id" : expression_id,
        "expression_info": {"content": "my expression",
                            "context" : "contesto",
                            "example_en": "example in english",
                            "example_it": "esempio in italiano",
                            "note": "note",
                            "translation_it": "traduzione",
                            "level": "A1",
                            "role": "Verbo",
                            "is_formal": "è formale",
                            "is_phrasal_verb": "è un phrasal verb"
                            },
        "User" : "username",
    }
    return render(request, "vocapp/expression.html", context)

def login(request):
    return render(request, "vocapp/login.html")

def signin(request):
    return render(request, "vocapp/signin.html")

def dashboard(request):
    context = {
        "not_learned" : 123,
        "learning" : 789,
        "learned" : 456,
        "User" : "username",
    }
    return render(request, "vocapp/dashboard.html", context)

def validation(request):
    # if from Login, then check credentials. If not found redirect to Login with error message.
    # if from Registration, then check if username already exists. If not, then create user. If yes, then redirect to Registration with error message.
    # if no error, redirect to Home.
    return HttpResponse("Validation")