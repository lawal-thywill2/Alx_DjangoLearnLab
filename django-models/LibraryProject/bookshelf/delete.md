# DELETE Operation Documentation

This document demonstrates how to delete a Book record using Django ORM.

## Command Used

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()