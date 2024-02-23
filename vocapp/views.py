from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. you are in the index")

def page1(request):
    return HttpResponse("Hi, you are in page1")