from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home1(request):
    return HttpResponse("Hello, welcome to the Project 1 index page!")