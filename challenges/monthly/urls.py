from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # path("january/", views.january),
    # path("february/", views.february),
    # path("march/", views.march),
    # path("<month>/", views.month_challenge),
    # path("<int:month>", views.month_challenges_number),
    # path("<str:month>", views.month_challenges_string),
    path("<month>", views.get_templates)


]
