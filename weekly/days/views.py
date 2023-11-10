from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
week_days = {
    "monday": "WOW, Monday",
    "tuesday": "2nd day of the week",
    "wednesday": "When this will end?",
    "thursday": "I'm almost finished",
    "friday": "It is almost the weekend",
    "saturday": "What?, we work 6 days per week",
    "sunday": "Weekend!!!!!!, Oh, tomorrow is Monday, when I will have a rest?",
}

days = list(week_days.keys())


def index(request):
    return render(request, 'index.html', {
        "days_name": days,
    })


def days_detail(request, day):
    days_detail = week_days[day]
    day = days_detail.capitalize()
    return render(request, 'day_detail.html', {
        "days_detail": days_detail,
        "day_name": day
    })
