from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views import View

from .models import ReviewsM
from .forms import FormReview


class ReviewView(View):
    def get(self, request):
        form = FormReview()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = FormReview(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thankyou")
        return render(request, "reviews/review.html", {
            "form": form
        })


class ThankYou(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Nice work"
        return context


# class ReviewList(TemplateView):
#     template_name = "reviews/review_list.html"
#     context_object_name = "reviews"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = ReviewsM.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewList(ListView):
    template_name = "reviews/review_list.html"
    context_object_name = "all_review"
    model = ReviewsM


class SingleReview(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = ReviewsM.objects.get(pk=review_id)
        context["review"] = selected_review
        return context

    # def get(self, request):
    #     return render(request, "reviews/thankyou.html")


# def thankyou(request):
#     return render(request, "reviews/thankyou.html")
# def reviews(request):
#     if request.method == "POST":
#         #form = Reviews(request.POST)
#         form = FormReview()  # add new
#         if form.is_valid():
#             # reviews = ReviewsM(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["comment"],
#             #     rating=form.cleaned_data["rating"]
#             # )
#             # reviews.save()
#             form.save()  # add new
#             return HttpResponseRedirect("/thankyou")
#     else:
#         form = FormReview()
#     return render(request, "reviews/review.html", {
#         "form": form
#     })


def arzuv(request):
    return render(request,"reviews/example.html")