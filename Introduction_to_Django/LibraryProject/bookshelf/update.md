# UPDATE Operation Documentation

This document demonstrates how to update an existing Book record using Django ORM.

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.published_year = 1950
book.save()

book