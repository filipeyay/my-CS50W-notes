from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def nikdra(request):
    return HttpResponse("Hello, Nikdra!")


def greet(request, name):
    # it's possible to give access of a variable to a template, this exemple we give acess to a dictionarie in the greet.html file
    return render(request, "hello/greet.html", {"name": name.capitalize()})
