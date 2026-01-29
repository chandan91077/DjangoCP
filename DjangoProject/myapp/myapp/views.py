from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Welcome to the home page.")
    return render(request, 'home.html')
def skill(request):
    # return HttpResponse("This is the skill page.")
    return render(request, 'skill.html')
def projects(request):
    # return HttpResponse("This is the projects page.")
    return render(request, 'projects.html')
def experience(request):
    # return HttpResponse("This is the experience page.")
    return render(request, 'experience.html')
def education(request):
    # return HttpResponse("This is the education page.")
    return render(request, 'education.html')
def contact(request):
    # return HttpResponse("This is the contact page.")
    return render(request, 'contact.html')