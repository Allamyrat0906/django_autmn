from django.contrib import admin

from books.models import Address, Author, Book, Country

# Register your models here.


class Beauty(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",), }
    list_filter = ("title", "rating")
    list_display = ("title", "author", "rating")


admin.site.register(Book, Beauty)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
