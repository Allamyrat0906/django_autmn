from django.urls import path
from . import views

app_name='blog_api'
urlpatterns = [
    path("<int:pk>/", views.ListDetail.as_view(),name="detailcreate"),
    path("",views.PostDetail.as_view(),name="listcreate")
]
