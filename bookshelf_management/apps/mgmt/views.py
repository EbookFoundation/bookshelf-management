from .models import Book, Bookshelf, BookshelfToBook
from django.http import HttpResponse


def booksInBookshelf(request, bookshelfId):
    idList = BookshelfToBook.objects.filter(fk_bookshelves=bookshelfId).values_list('fk_books', flat=True) 
    books = Book.objects.filter(id__in=idList)
    return HttpResponse(books)
