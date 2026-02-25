import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. List all books in a library
library_name = "Central Library"   # or any real library name in your DB
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(book.title)

# 2. Query all books by a specific author
author_name = "Chinua Achebe"  # or any
author = Author.objects.get(name=author_name)  # replace with an actual author name in your DB
books_by_author = Book.objects.filter(author=author)

print("Books by Chinua Achebe:")
for book in books_by_author:
    print(book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print(f"\nLibrarian of {library.name}:")
print(librarian.name)