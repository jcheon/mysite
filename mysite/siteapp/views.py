from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    context={
        "name": "Jonathan Cheon",
        "description": "Some elaborate statement about myself here ya feel",
        "twitter": "https://twitter.com/jcheon4",
        "linkedin": "https://linkedin.com/in/jcheon",
        "github": "https://github.com/jcheon",
    }
    return render(request, "index.html", context=context)

def resume(request):
    context={
    }
    return render(request, "resume.html", context=context)

def projects(request):
    context={
    }
    return render(request, "projects.html", context=context)