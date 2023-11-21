from django.urls import path
from . import views

urlpatterns = [
    path("", views.reviews),
    path("thankyou", views.thankyou, name="thankyou")
]
