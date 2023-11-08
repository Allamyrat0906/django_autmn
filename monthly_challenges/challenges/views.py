from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from django.template.loader import render_to_string

monthly_chanllenge = {
    "january": "Eat no meat for the entire month",
    "february": "walk for at least 20minutes  evary day",
    "march": "march is also cool month",
    "april": "April is my favorite month",
    "may": "May decide about whether ",
    "june": "June is my birthday",
    "jule": "july is very hot month",
    "august": "august month it  is good month for rest in the beavh",
    "september": "this  month started  all education",
    "october": "this month my new girlfriend birthday",
    "november": "novber month just sleep",
    "december": None
}


def index(request):

    months = list(monthly_chanllenge.keys())

    # for month in months:
    #     capetalize_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_item += f"<li><a href='{month_path}'>{capetalize_month}</a></li>"

    # response_data = f"<ul>{list_item}</ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


def month_number(request, month):
    months = list(monthly_chanllenge.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month_dict(request, month):
    try:
        challenges_text = monthly_chanllenge[month]
        # response_data = f"<h1>{challenges_text}</h1>"
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenges_text,
            "month_name": month.capitalize()
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        return HttpResponseNotFound("not founded")


###################################################################
# def january(request):
#     return HttpResponse("Eat no meat for the entire month")

###################################################################
# def february(request):
#     return HttpResponse("walk for at least 20minutes  evary day")
###################################################################
# def month_number(request, month):
#     return HttpResponse(month)
###################################################################

###################################################################
# def month_challenge(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "Eat no meat for the entire month"
#     elif month == "february":
#         challenge_text = "walk for at least 20minutes  evary day"
#     else:
#         return HttpResponseNotFound("This month not sopperted")
#     return HttpResponse(challenge_text)

###################################################################
