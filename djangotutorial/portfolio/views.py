from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def portfolio(request):
    return HttpResponse("This is my portfolio page.")