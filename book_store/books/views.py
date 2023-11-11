from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from books.models import Books

# Create your views here.


def all_books(request):
    books = Books.objects.all()
    return render(request, "books/all_books.html", {
        "books": books
    })


def book_detail(request, id):
    book_detail = get_object_or_404(Books, pk=id)
    #book_detail = Books.objects.get(pk=id)
    return render(request, "books/book_detail.html",
                  {
                      "book_detail": book_detail
                  })
