
from django.urls import path
from . import views

urlpatterns = [
    path("",views.ShowPost.as_view()),
]
