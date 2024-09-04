from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def index(request):
    return redirect('books')

def book_show(request, date):
    books = list(Book.objects.all())
    books.sort(key=lambda x: x.pub_date)
    current_number_book = [i for i, h in enumerate(books) if h.pub_date==date][0]
    paginator = Paginator(books, 1)
    page = paginator.get_page(current_number_book+1)
    template = 'books/books_list.html'
    books = [Book.objects.filter(pub_date=date).first()]
    context = {'books': books,
               'page': page,
               'next':paginator.get_page(current_number_book+2),
               'last': paginator.get_page(current_number_book)}
    return render(request, template, context)
