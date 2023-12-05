from django.urls import path
from . import views


urlpatterns = [
    path("",views.UserCreateList.as_view(),name="create-user"),
    path("<int:pk>",views.UserUpdateDelte.as_view(),name="update-delete")
]
