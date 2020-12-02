from django.contrib import admin

from .models import Bookshelf, Book

admin.site.register(Bookshelf)
admin.site.register(Book)
