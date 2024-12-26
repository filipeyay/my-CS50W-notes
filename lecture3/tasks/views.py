from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


tasks = []


# Create your views here.
def index(request):
    # defines that 2 users cannot see the same list
    # separating the lists by sessions
    if "tasks" not in request.session:
        # if the user does not already have a task list, give him an empty list
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {"tasks": request.session["tasks"]})


def add(request):
    # logic to add tasks
    if request.method == "POST":
        # request.POST contains all the data that the user sends, when he sends it
        form = NewTaskForm(request.POST)
        # if the form is valid, get the 'data' from "tasks", store it in a variable called "task" and then add it to the list
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # redirect the user to the task list after inserting a new task
            return HttpResponseRedirect(reverse("index"))
        # if something is wrong the error is shown to the user
        else:
            return render(request, "tasks/add.html", {"form": form})
    # If nothing is entered then it just reloads an empty 'form' for the user
    return render(request, "tasks/add.html", {"form": NewTaskForm()})


# to finally be able to run the server, we need to do the "migrate" process with `python manage.py migrate`
# this command will allow us to create all the standard "tables" within the django database
