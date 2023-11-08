from django.urls import path
from . import views


urlpatterns = [
    # path("january", views.january),
    # path("february",views.february)

    # path("<int:month>", views.month_number),
    # path("<str:month>", views.month_challenge),
    path("", views.index, name="index"),
    path("<int:month>", views.month_number),
    path("<str:month>", views.month_dict, name="month-challenge"),
]
