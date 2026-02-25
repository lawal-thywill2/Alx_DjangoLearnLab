import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)

print("Books by Chinua Achebe:")
for book in books_by_author:
    print(book.title)

# 2. List all books in a library
library =Library.objects.get(name="library_name")
books_in_library = library.books.all()

print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print("\nLibrarian of Central Library:")
print(librarian.name)