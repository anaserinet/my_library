from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random
from .models import Book
from .forms import BookForm


def welcome(request):
    """Render the welcome page for users."""
    slogans = [
        'Love the library and knowledge will love you',
        'Having fun is not hard when you have a library card',
        'Libraries make shh happen',
        'Believe in your shelf'
    ]
    random_display = random.choice(slogans)

    context = {'slogan': random_display}
    return render(request, 'welcome.html', context)


def books(request):
    """Returns list of books in db for display"""
    books_listed = Book.objects.all()
    context = {'books_list': books_listed}
    return render(request, 'books.html', context)


def get_book(request, book_id):
    return HttpResponse(f"You are requesting a book with book_id {book_id}")


def get_book2(request, book_id, foo):
    return HttpResponse(f"You are requesting a book with book_id {book_id}, foo: {foo}")


def get_book3(request, book_id):
    foo = request.GET.get('foo', 0)
    bar = request.GET.get('bar', 0)
    return HttpResponse(f"You are requesting a book with book_id {book_id}, foo: {foo}, bar:{bar}")

# 3 paths through this view function.
# get request == 'Get'
# post request with invalid data: if the form is not valid, it will not let us submit it
# if the post request is valid: a book object is created and saved (you can see the new book that you sumbited added to the /books/ path)
# try and accept block: if for some reason the book has some sort of conflicting data (like for example you try to submit a book with a isbn num that already exists in your DB) it will catch the error, not save the book and instead print a message


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # Old code from when we used form instead of ModelForm
            # authors = form.cleaned_data['authors']
            # title = form.cleaned_data['title']
            # publication_date = form.cleaned_data['publication_date']
            # isbn = form.cleaned_data['isbn']
            # book = Book(authors=authors, title=title, publication_date=publication_date, isbn=isbn)
            try:
                # book.save()
                form.save()
            except:
                form.add_error(None, "It was not possible to save this book")

            # only redirects if input to DB is valid
            else:
                # (we shouldnt hardcode paths), so we use the reverse lib function
                path = reverse('books')
                return HttpResponseRedirect(path)
    else:
        form = BookForm()

    return render(request, 'create_book.html', {'form': form})
