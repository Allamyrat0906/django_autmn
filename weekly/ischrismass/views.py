from django.shortcuts import render
import datetime
# Create your views here.


def newyear(request):
    now = datetime.datetime.now()
    return render(request, "base/newyear.html", {
        "isnewyear": now.month == 1 and now.day == 1
    })
