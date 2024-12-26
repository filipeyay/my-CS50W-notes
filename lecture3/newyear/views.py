from django.shortcuts import render
import datetime

# Create your views here.


# Let's use the 'datetime' module to verify if it's new year
def index(request):
    now = datetime.datetime.now()
    return render(
        request,
        "newyear/index.html",
        {
            # "newyear": True
            "newyear": now.month == 1
            and now.year == 1
        },
    )
