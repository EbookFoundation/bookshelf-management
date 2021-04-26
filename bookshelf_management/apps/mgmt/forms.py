
from django import forms
from .models import Book

class NewBookForm(forms.Form):
    bookid = forms.CharField(label='Book ID', max_length=12)
    def is_valid():
        return Book.objects.get(self.bookid) != None


class BookSearchForm(forms.Form):
    searchTerm = forms.CharField(label='Search Term', max_length=64)
    def is_valid():
        return str(searchTerm) != ''
           

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=64, widget=forms.PasswordInput())
    def is_valid():
        return str(username) != '' and str(password) != ''
           




