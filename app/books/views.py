from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg
from .forms import BookForm
from .models import Book, Author


# Create your views here.
def index(request):
    """List all books"""
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "books/index.html", {
        "books": books,
        "total_number": num_books,
        "average_rating": avg_rating
    })

def book_detail(request, slug):
    """Get a single book"""
    book = get_object_or_404(Book, slug=slug)
    return render(request, "books/book_detail.html", {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "os_bestselling": book.is_bestselling
    })


def create_book(request, pk):
    """Create a book"""
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=book.id)
        else:
            return render(request, "books/partials/book_form.html", context={
                "form": form
            })


    context = {
        "form": form,
        "author": author,
        "books": books,
        "title": "Create a book"
    }

    return render(request, "books/create_book.html", context)

def create_book_form(request):
    """Return the form for HTMX create form"""
    form = BookForm()
    context = {
        "form": form
    }

    return render(request,"books/partials/book_form.html", context)

def detail_book(request,pk):
    book = get_object_or_404(Book, id=pk)
    context = {
        "book": book
    }

    return render(request, "books/partials/book_detail.html", context)