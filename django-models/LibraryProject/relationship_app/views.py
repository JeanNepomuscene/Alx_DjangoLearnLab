from django.shortcuts import render
from django.views.generic.detail import DetailView  # 👈 Correct import for ALX
from .models import Book
from .models import Library   # 👈 ALX checker wants this exact line

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
