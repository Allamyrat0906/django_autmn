from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thankyou", views.ThankYou.as_view(), name="thankyou"),
    path("reviews", views.ReviewList.as_view()),
    path("reviews/<int:id>", views.SingleReview.as_view()),
    path("arzuv",views.arzuv)
]
