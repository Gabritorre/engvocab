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
		return HttpResponseRedirect(reverse("vocapp:home"))
	
	# if there is no user logged in just redirect to home
	return redirect('vocapp:home')

def update_filters(request):
	request.session["level_filters"] = []
	request.session["phrasal"] = False
	request.session["category"] = "discover"
	print(dict(request.GET))
	if ("level" in request.GET):
		request.session["level_filters"] = dict(request.GET)["level"]

	if ("phrasal" in request.GET):
		request.session["phrasal"] = True

	if ("category" in request.GET):
		request.session["category"] = request.GET["category"]

	return HttpResponseRedirect(reverse("vocapp:home"))

def home(request):
	levels = Level.objects.values_list('level', flat = True)
	if ("level_filters" not in request.session.keys()):
		request.session["level_filters"] = []
	
	if ("phrasal" not in request.session.keys()):
		request.session["phrasal"] = False
	
	if ("category" not in request.session.keys()):
		request.session["category"] = "discover"

	# se discovery allora prendi expression non ancora legate alla tabella Learn
	# se review allora prendi expression solamente collegate alla tabella Learn
	# controllo se l'utente è autenticato(?)
	# se non è collegato è discovery di default
	if (request.session["level_filters"] == []):
		if (request.session["phrasal"]):
			filtered_ids = Expression.objects.filter(is_phrasal_verb = True).values_list('id', flat = True)
		else:
			filtered_ids = Expression.objects.values_list('id', flat = True)
	else:
		if (request.session["phrasal"]):
			filtered_ids = Expression.objects.filter(is_phrasal_verb = True, level__in=request.session["level_filters"]).values_list('id', flat=True)
		else:
			filtered_ids = Expression.objects.filter(level__in=request.session["level_filters"]).values_list('id', flat=True)

	expression_data = Expression.objects.get(pk = choice(filtered_ids))	# pick a random expression respecting the filters
	context = {
		"levels": levels,
		"phrasal": request.session["phrasal"],
		"expression_info": expression_data,
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
		not_learned = Learn.objects.filter(user=request.user.id, confidence__lte=0).count()
		learning = Learn.objects.filter(user=request.user.id, confidence__range=(1, 10)).count()
		learned = Learn.objects.filter(user=request.user.id, confidence__gte=11).count()
		context = {
			"not_learned" : not_learned,
			"learning" : learning,
			"learned" : learned,
		}
		return render(request, "vocapp/dashboard.html", context)
	else:
		return redirect("vocapp:login_user")

def signup(request):
	if request.user.is_authenticated:
		return redirect("vocapp:home")
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("vocapp:login_user"))
	else:
		form = SignupForm()
	return render(request, "vocapp/signup.html", {'form': form})

def login_user(request):
	if request.user.is_authenticated:
		return redirect("vocapp:home")
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