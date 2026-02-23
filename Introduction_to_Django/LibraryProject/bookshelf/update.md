# UPDATE Operation Documentation

This document demonstrates how to update an existing Book record using Django ORM.

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title, "Nineteen Eighty-Four"
book.save()

book