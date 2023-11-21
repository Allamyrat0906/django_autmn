from django.shortcuts import render, HttpResponseRedirect
from .forms import Reviews


def reviews(request):

    # if request.method == "POST":
    #     entered_username = request.POST['username']
    #     print(entered_username)
    #     if entered_username == "":
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })

    #     return render(request, "reviews/thankyou.html")
    #     # return HttpResponseRedirect("/thankyou")
    # return render(request, "reviews/review.html",)
    if request.method == "POST":
        form = Reviews(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thankyou")
    else:
        form = Reviews()
    return render(request, "reviews/review.html", {
        "form": form
    })


def thankyou(request):
    return render(request, "reviews/thankyou.html")
