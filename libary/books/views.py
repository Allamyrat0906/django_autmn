from django.http import Http404
from django.shortcuts import render
from books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "libary/index.html", {
        "books": books
    })


def book_detail(request, slug):
    try:
        book_detail = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "libary/book_detail.html", {
        "book_detail": book_detail
    })
