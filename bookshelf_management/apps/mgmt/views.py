from .models import Book, Bookshelf, BookshelfToBook
from django.http import HttpResponse
from django.shortcuts import render


from django.views import generic

# class BookListView(generic.ListView):
#     model = Book

    



def booksInBookshelf(request, bookshelfId):
    bookshelfName = Bookshelf.objects.get(id=bookshelfId).bookshelf
    idList = BookshelfToBook.objects.filter(fk_bookshelves=bookshelfId).values_list('fk_books', flat=True) 
    books = Book.objects.filter(id__in=idList)

    context = {
        'books': books,
        'total': len(books),
        'bookshelf': bookshelfName,
    }


    return render(request, 'index.html', context=context)
