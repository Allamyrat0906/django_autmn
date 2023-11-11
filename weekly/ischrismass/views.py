from django.shortcuts import render
import datetime
# Create your views here.


def newyear(request):
    now = datetime.datetime.now()
    isnewyear = (now.month == 1 and now.day == 1)
    return render(request, "base/newyear.html", {
        "isnewyear": isnewyear
    })
