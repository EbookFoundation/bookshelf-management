from django.contrib import admin

from .models import Bookshelf, Book, BookshelfToBook

admin.site.register(Bookshelf)
admin.site.register(Book)
admin.site.register(BookshelfToBook)
