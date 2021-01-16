from django.shortcuts import render

import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "naadam/index.html", {
        "naadam": now.month == 7 and now.day == 11 or now.month == 7 and now.day == 12 or now.month == 7 and now.day == 13
        # "naadam": True
    })