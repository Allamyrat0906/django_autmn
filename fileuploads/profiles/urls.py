from django.urls import path
from . import views 


urlpatterns = [
    path("profiles/",views.CreateProfileView.as_view() , name="profile"),
    path("list/",views.UserProfilesView.as_view(), name="user_profiles")
]
