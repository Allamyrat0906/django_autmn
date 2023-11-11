from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_books, name="all-books"),
    path("<int:id>", views.book_detail, name="book-detail")
]
