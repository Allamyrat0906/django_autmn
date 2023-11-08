from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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
    "december": None
}


def index(request):
    months = list(challenges_dict.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def month_number(request, month):
    months = list(challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month_dict(request, month):
    try:
        challenges_text = challenges_dict[month]
        # response_data = f"<h1>{challenges_text}</h1>"
        # return HttpResponse(response_data)

        return render(request, "challenges.html", {
            "text": challenges_text,
            "month_name": month.capitalize()
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        return HttpResponseNotFound("not founded")
