# RETRIEVE (READ) Operation Documentation

This document demonstrates how to retrieve Book records from the database using Django ORM.

## Command Used

```python
from bookshelf.models import Book

Book.objects.all()