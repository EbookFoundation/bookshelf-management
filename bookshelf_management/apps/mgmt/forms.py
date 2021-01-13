
from django import forms
from .models import Book

class NewBookForm(forms.Form):
    bookid = forms.CharField(label='Book ID', max_length=12)
    def is_valid():
        return Book.objects.get(self.bookid) != None
           




