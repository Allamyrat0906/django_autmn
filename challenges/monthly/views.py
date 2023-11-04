from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


challenges_dict = {
    "january": "this month walks more",
    "february": "this month february",
    "march": "this month march",
    "april": "this month april",
    "may": "this month may",
    "june": "this month june",
    "july": "this month july",
    "autumn": "this month autumn",
    "september": "this month september",
    "october": "this month october",
    "november": "this month november",
    "december": "this month december",
}


def index(request):
    return HttpResponse("hi")


def january(request):
    return HttpResponse("coming januray")


def february(request):
    return HttpResponse("coming february")


def march(request):
    return HttpResponse("coming march")


def month_challenge(request, month):
    # return HttpResponse(month)
    text_challenges = None
    if month == "january":
        text_challenges = "january month"
    elif month == "february":
        text_challenges = "february month"
    elif month == "march":
        text_challenges = "march month"
    else:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(text_challenges)

# number


def month_challenges_number(request, month):

    list_month_challenges = list(challenges_dict.keys())
    if len(list_month_challenges) >= month:
        months = list_month_challenges[month-1]
        return HttpResponse(months)
    else:
        return HttpResponseNotFound("month only contains 12 numbers")

# string


def month_challenges_string(request, month):
    list_month_challenges = challenges_dict[month]
    return HttpResponse(list_month_challenges)


def get_templates(request, month):
    list_month_challenges = challenges_dict[month]
    return HttpResponse(f"<h1>{ list_month_challenges}</h1>")
