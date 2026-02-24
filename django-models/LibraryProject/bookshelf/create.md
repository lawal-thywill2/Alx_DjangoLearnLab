# CREATE Operation Documentation

This document demonstrates how to create a Book record using Django ORM.

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_year=1949
)

book