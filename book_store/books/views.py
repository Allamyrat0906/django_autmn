from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from books.models import Books

# Create your views here.


def all_books(request):
    books = Books.objects.all()
    return render(request, "books/all_books.html", {
        "books": books
    })


def book_detail(request, slug):
    book_instance = get_object_or_404(Books, slug=slug)
    return render(request, "books/book_detail.html",
                  {"book_instance": book_instance})
