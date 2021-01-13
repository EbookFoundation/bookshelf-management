from .models import Book, Bookshelf, BookshelfToBook
from django.http import HttpResponse
from django.shortcuts import render



from .forms import NewBookForm
from django.views import generic

# class BookListView(generic.ListView):
#     model = Book

    
def insertBookToBookshelf(bookId, bookshelfId):
    newEntry = BookshelfToBook.objects.create(bookId, bookshelfId)
    newEntry.save()


def booksInBookshelf(request, bookshelfId):
    bookshelfName = Bookshelf.objects.get(id=bookshelfId).bookshelf
    idList = BookshelfToBook.objects.filter(fk_bookshelves=bookshelfId).values_list('fk_books', flat=True) 
    books = Book.objects.filter(id__in=idList)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = (request.POST)
        print(form)
        # check whether it's valid:
        if form.bookid != None:
            insertBookToBookshelf(form.bookid, bookshelfId)
            # redirect to a new URL:
            return render(request, 'index.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewBookForm()

    context = {
        'books': books,
        'total': len(books),
        'bookshelf': bookshelfName,
        'bookshelfId': bookshelfId,
        'form': form
    }


    return render(request, 'index.html', context=context)


def bookshelfList(request):
    bookshelves = Bookshelf.objects.all()

    context = {
        'bookshelves': bookshelves,
        'total': len(bookshelves),
    }


    return render(request, 'bookshelfList.html', context=context)


def get_name(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = (request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return 

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewBookForm()

    return render(request, 'name.html', {'form': form})
