import os
import django

# Setup Django environment for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- 1. Query all books by a specific author ---
author_name = "J.K. Rowling"  # change as needed
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# --- 2. List all books in a library ---
library_name = "Central Library"  # change as needed
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in library_books]}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# --- 3. Retrieve the librarian for a library ---
try:
    librarian = library.librarian  # thanks to OneToOneField
    print(f"Librarian for {library.name}: {librarian.name}")
except AttributeError:
    print(f"{library_name} has no librarian assigned yet")
