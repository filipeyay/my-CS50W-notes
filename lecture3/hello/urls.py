from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nikdra", views.nikdra, name="nikdra"),
    # takes the name parameter, ensures it is a string and uses the url to display the name to the user
    path("<str:name>", views.greet, name="greet"),
]
