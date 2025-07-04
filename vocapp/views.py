from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from django.utils.html import escape
from .forms import LoginForm, SignupForm

from .models import *
from .custom_exceptions import EmptyQuery
from random import choice

import json
import re


CONFIDENCE_BAR = 420
CONFIDENCE_PARAMETERS = {
	"A1/A2": 140,
	"B1" : 84,
	"B1+" : 60,
	"B2" : 42,
	"C1/C2" : 35
}
FORCED_EXPRESSION_ID = None
VALID_REPORT_FIELDS = {'content', 'transl', 'note', 'context', 'expl', 'expl_it', 'phrasal', 'formal', 'figurative', 'role', 'lvl'}


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
		for level in dict(request.GET)["level"]:
			if level in CONFIDENCE_PARAMETERS.keys():
				request.session["level_filters"].append(level)

	if ("phrasal" in request.GET):
		request.session["phrasal"] = True

	if ("category" in request.GET):
		if request.GET["category"] == "review":
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


def get_other_translations(expression):
	match = re.search(r'\((\d+)\)', expression.content)
	if match:	# if the expression contains "(<number>)"
		number = match.group(1) # extract the number
		word = expression.content.split(f' ({number})')[0]  # get the word before the number
		return Expression.objects.filter(content__icontains=f'{word} (').exclude(id=expression.id) # get the other translations of the same word
	else:
		return []


def home(request):
	global FORCED_EXPRESSION_ID
	levels = Level.objects.values_list('level', flat = True)

	if FORCED_EXPRESSION_ID:
		context = {
			"levels": levels,
			"expression_info": Expression.objects.get(pk = FORCED_EXPRESSION_ID),
			"other_translations": get_other_translations(Expression.objects.get(pk = FORCED_EXPRESSION_ID)),
			"error" : {}
		}
		FORCED_EXPRESSION_ID = None
		return render(request, "vocapp/home.html", context)

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
			"other_translations": [],
			"error": e,
		}
	else:
		context = {
			"levels": levels,
			"expression_info": expression_data,
			"other_translations": get_other_translations(expression_data),
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
	global FORCED_EXPRESSION_ID
	expression_info = Expression.objects.get(pk = expression_id)
	if FORCED_EXPRESSION_ID:
		FORCED_EXPRESSION_ID = None
	context = {
		"expression_id" : expression_id,
		"expression_info": expression_info,
		"other_translations": get_other_translations(expression_info),
	}
	return render(request, "vocapp/expression.html", context)


# check if the redirect_url is from expression page or home page
def validate_redirect(request, redirect_url):
	home_url = request.build_absolute_uri(reverse("vocapp:home"))
	expression_url = request.build_absolute_uri(reverse("vocapp:inspect_expression", kwargs={"expression_id": 0}))
	expression_url = expression_url.replace("/0", "/")

	if redirect_url == home_url or redirect_url.startswith(expression_url):
		return True
	else:
		return False


def report(request, expression_id):
	global FORCED_EXPRESSION_ID
	global VALID_REPORT_FIELDS
	if not validate_redirect(request, request.META.get('HTTP_REFERER', '/')):
		return redirect("vocapp:home")
	if request.user.is_authenticated:
		if request.method == "POST":
			if "message" not in request.POST or "involved_fields" not in request.POST:
				FORCED_EXPRESSION_ID = expression_id
				return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
			fields_string = ""
			for field in request.POST.getlist("involved_fields"):
				if field in VALID_REPORT_FIELDS:
					fields_string += field + "-"
			expression = Expression.objects.get(pk = expression_id)
			message = escape(request.POST["message"])
			report = Report(user = request.user, expression = expression, fields = fields_string, message = message)
			report.save()
			FORCED_EXPRESSION_ID = expression_id
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def progress(request):
	# check if user is autenticated, if not redirect to home
	if request.user.is_authenticated:
		discovered_ids = Learn.objects.filter(user_id = request.user.id).values_list('expression_id', flat=True)
		never_seen = Expression.objects.exclude(id__in=discovered_ids).count()
		learning = Learn.objects.filter(user=request.user.id, confidence__range=(0, CONFIDENCE_BAR-1)).count()
		learned = Learn.objects.filter(user=request.user.id, confidence__gte=CONFIDENCE_BAR).count()
		expressions_by_level = Expression.objects.values('level').annotate(total=models.Count('level'))
		learning_expressions_by_level = Learn.objects.filter(user=request.user.id, confidence__lt=CONFIDENCE_BAR).values('expression__level').annotate(total=models.Count('expression__level'))
		learned_expressions_by_level = Learn.objects.filter(user=request.user.id, confidence__gte=CONFIDENCE_BAR).values('expression__level').annotate(total=models.Count('expression__level'))
		never_seen_expressions_by_level = Expression.objects.exclude(id__in=discovered_ids).values('level').annotate(total=models.Count('level'))

		never_seen_expressions_by_level = {item['level']: item['total'] for item in never_seen_expressions_by_level}
		expressions_by_level = {item['level']: item['total'] for item in expressions_by_level}
		learning_expressions_by_level = {item['expression__level']: item['total'] for item in learning_expressions_by_level}
		learned_expressions_by_level = {item['expression__level']: item['total'] for item in learned_expressions_by_level}
		levels = Level.objects.values_list('level', flat = True)
		levels = {level: (never_seen_expressions_by_level.get(level, 0), learning_expressions_by_level.get(level, 0), learned_expressions_by_level.get(level, 0), expressions_by_level[level]) for level in levels}


		never_seen_expression_list = Expression.objects.exclude(id__in=discovered_ids).order_by('content')
		learning_expression_list = Expression.objects.filter(learn__user=request.user.id, learn__confidence__lt=CONFIDENCE_BAR).order_by('content')
		learned_expression_list = Expression.objects.filter(learn__user=request.user.id, learn__confidence__gte=CONFIDENCE_BAR).order_by('content')
		context = {
			"never_seen" : never_seen,
			"learning" : learning,
			"learned" : learned,
			"total_expressions": never_seen + learning + learned,
			"levels": levels,
			"never_seen_expression_list": never_seen_expression_list,
			"learning_expression_list": learning_expression_list,
			"learned_expression_list": learned_expression_list,
		}
		return render(request, "vocapp/progress.html", context)
	else:
		return redirect("vocapp:login_user")


def about(request):
	context = {
		"version" : "2.4.0",
		"repo" : "https://github.com/Gabritorre/engvocab",
	}
	return render(request, "vocapp/about.html", context)

def profile(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			if "username" in request.POST and request.POST["username"]:
				new_username = request.POST["username"]
				if new_username == request.user.username:
					return render(request, "vocapp/profile.html", {"ref":"username", "status":"ERROR", "response": "Username not changed."})
				if User.objects.filter(username=new_username).exists():
					return render(request, "vocapp/profile.html", {"ref":"username", "status":"ERROR", "response": "Username already exists."})
				request.user.username = new_username
				request.user.save()
				return render(request, "vocapp/profile.html", {"ref":"username", "status":"OK", "response": "Username updated successfully."})
			elif "password" in request.POST and request.POST["password"]:
				if request.POST["password"] != request.POST["password_conf"]:
					return render(request, "vocapp/profile.html", {"ref":"password", "status":"ERROR", "response": "Passwords do not match."})
				request.user.set_password(request.POST["password"])
				request.user.save()
				return render(request, "vocapp/profile.html", {"ref":"password", "status":"OK", "response": "Password updated successfully. Login required."})
		return render(request, "vocapp/profile.html", {"ref": None, "status": None, "response": None})
	else:
		return redirect("vocapp:login_user")
	

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
		
		# If form is not valid or user already exists, return to signup page with error
		form = SignupForm()
		if User.objects.filter(username=request.POST["username"]).exists():
			return render(request, "vocapp/signup.html", {'form': form, 'status': "ERROR", 'response': "Username already exists."})
		if request.POST["password1"] != request.POST["password2"]:
			return render(request, "vocapp/signup.html", {'form': form, "status":"ERROR", "response": "Passwords do not match."})
	else:
		form = SignupForm()
	return render(request, "vocapp/signup.html", {'form': form, 'status': None, 'response': None})


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
		return render(request, "vocapp/login.html", {'form': form, 'status': "ERROR", 'response': "Invalid credentials."})
	else:
		form = LoginForm()
	return render(request, "vocapp/login.html", {'form': form, 'status': None, 'response': None})


def logout_user(request):
	logout(request)
	return redirect("vocapp:login_user")