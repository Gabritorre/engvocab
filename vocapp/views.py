from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def redir_home(request):
    return redirect('home')

def home(request):
    context = {
        "levels": ["A1/A2", "B1", "B1+", "B2", "C1"],
        "categories": ["Idiom", "Phrasal Verb"],
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
        "User" : "Gigi",
    }
    return render(request, "vocapp/home.html", context)

def search(request):
    context = {
        "User" : "Gigi",
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
        "User" : "Gigi",
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
        "User" : "Gigi",
    }
    return render(request, "vocapp/dashboard.html", context)

def validation(request):
    # if from Login, then check credentials. If not found redirect to Login with error message.
    # if from Registration, then check if username already exists. If not, then create user. If yes, then redirect to Registration with error message.
    # if no error, redirect to Home.
    return HttpResponse("Validation")