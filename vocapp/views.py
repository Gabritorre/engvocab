from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from .forms import LoginForm, SignupForm

from .models import Role, Level, Expression, Learn, User
from .custom_exceptions import EmptyQuery
from random import choice

import json

CONFIDENCE_BAR = 420
CONFIDENCE_PARAMETERS = {
	"A1/A2": 140,
	"B1" : 84,
	"B1+" : 60,
	"B2" : 42,
	"C1/C2" : 35
}

def redir_home(request):
    return redirect('vocapp:home')

def adjust_confidence(request, expression_id):
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)
		expr = Expression.objects.get(pk = expression_id)
		try:
			association = Learn.objects.get(user = user, expression = expr)
			if (request.POST["guessing"] == '1'):	# guessed
				association.confidence += CONFIDENCE_PARAMETERS[str(expr.level)]
			association.save()
		except Learn.DoesNotExist:	# create a new association between user and expression
			if (request.POST["guessing"] == '1'):	# guessed
				new_association = Learn(user = user, expression = expr, confidence=CONFIDENCE_PARAMETERS[str(expr.level)])
			else:
				new_association = Learn(user = user, expression = expr, confidence=0)
			new_association.save()
		return HttpResponseRedirect(reverse("vocapp:home"))

	# if there is no user logged in just redirect to home
	return redirect('vocapp:home')

def update_filters(request):
	request.session["level_filters"] = []
	request.session["phrasal"] = False
	request.session["category"] = "discover"
	if ("level" in request.GET):
		request.session["level_filters"] = dict(request.GET)["level"]

	if ("phrasal" in request.GET):
		request.session["phrasal"] = True

	if ("category" in request.GET):
		request.session["category"] = request.GET["category"]

	return HttpResponseRedirect(reverse("vocapp:home"))

def filter_expressions(levels, phrasal, category, user):
	expressions_set = None

	# DISCOVER or REVIEW
	if category == "review" and user.is_authenticated:
		expressions_set = Expression.objects.filter(learn__user_id = user.id, learn__confidence__gte = 0)
		if not expressions_set:
			raise EmptyQuery(1)
	elif category == "discover" and user.is_authenticated:
		discovered_ids = Learn.objects.filter(user_id = user.id).values_list('expression_id', flat=True)
		expressions_set = Expression.objects.exclude(id__in=discovered_ids)
		if not expressions_set:
			raise EmptyQuery(2)
	else:
		expressions_set = Expression.objects.all()
		if not expressions_set:
			raise EmptyQuery(3)

	# LEVEL FILTERS and PHRASAL VERB
	if (levels == []):
		if (phrasal):
			filtered_ids = expressions_set.filter(is_phrasal_verb = True).values_list('id', flat = True)
			if not filtered_ids:
				raise EmptyQuery(4)
		else:
			filtered_ids = expressions_set.values_list('id', flat = True)
			if not filtered_ids:
				raise EmptyQuery(5)
	else:
		if (phrasal):
			filtered_ids = expressions_set.filter(is_phrasal_verb = True, level__in=levels).values_list('id', flat=True)
			if not filtered_ids:
				raise EmptyQuery(6)
		else:
			filtered_ids = expressions_set.filter(level__in=levels).values_list('id', flat=True)
			if not filtered_ids:
				raise EmptyQuery(7)
			
	if not filtered_ids:
		raise EmptyQuery(0)
	
	return expressions_set.get(pk = choice(filtered_ids))


def home(request):
	levels = Level.objects.values_list('level', flat = True)
	if ("level_filters" not in request.session.keys()):
		request.session["level_filters"] = []
	
	if ("phrasal" not in request.session.keys()):
		request.session["phrasal"] = False
	
	if ("category" not in request.session.keys()):
		request.session["category"] = "discover"

	try:
		expression_data = filter_expressions(request.session["level_filters"], request.session["phrasal"], request.session["category"], request.user)
	except EmptyQuery as e:
		context = {
			"levels": levels,
			"expression_info": {},
			"error": e,
		}
	else:
		context = {
			"levels": levels,
			"expression_info": expression_data,
			"error" : {}
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


def progress(request):
	# check if user is autenticated, if not redirect to home
	if request.user.is_authenticated:
		discovered_ids = Learn.objects.filter(user_id = request.user.id).values_list('expression_id', flat=True)
		not_learned = Expression.objects.exclude(id__in=discovered_ids).count()
		learning = Learn.objects.filter(user=request.user.id, confidence__range=(0, CONFIDENCE_BAR-1)).count()
		learned = Learn.objects.filter(user=request.user.id, confidence__gte=CONFIDENCE_BAR).count()
		context = {
			"not_learned" : not_learned,
			"learning" : learning,
			"learned" : learned,
			"total_expressions": not_learned + learning + learned,
		}
		return render(request, "vocapp/progress.html", context)
	else:
		return redirect("vocapp:login_user")

def about(request):
	context = {
		"version" : "2.0.0",
		"repo" : "https://github.com/Gabritorre/engvocab",
	}
	return render(request, "vocapp/about.html", context)

def signup(request):
	if request.user.is_authenticated:
		return redirect("vocapp:home")
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			form.save()
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				return redirect("vocapp:home")
			return HttpResponseRedirect(reverse("vocapp:signup_user"))
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