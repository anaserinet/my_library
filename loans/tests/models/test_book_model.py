from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

import datetime

from loans.models import Book


class BookTestCase(TestCase):
    def setUp(self):
        authors = 'Doe J.'
        title = 'A title'
        publication_date = datetime.datetime(2024, 9, 1)
        isbn = '123456190'
        self.book = Book(authors=authors, title=title,
                         publication_date=publication_date, isbn=isbn)

    # checks wether the default model is valid
    def test_valid_book_is_valid(self):
        try:
            self.book.full_clean()
        except ValidationError:
            self.fail('Default test book should be deemed valid')

    # verifies that an invalid book object is indeed invalid
    def test_book_with_blank_author_is_invalid(self):
        self.book.authors = ''
        with self.assertRaises(ValidationError):
            self.book.full_clean()

    # verifies that an invalid book object is indeed invalid
    def test_book_with_blank_author_is_invalid(self):
        self.book.authors = 'x' * 256
        with self.assertRaises(ValidationError):
            self.book.full_clean()

    # checks that you cant insert 2 books with the same isbn
    def test_book_isbn_must_be_unique(self):
        self.book.save()
        authors = 'Pickles, P.'
        title = 'Another title'
        publication_date = datetime.datetime(2024, 9, 1)
        isbn = '123456190'
        with self.assertRaises(IntegrityError):
            Book.objects.create(authors=authors, title=title,
                                publication_date=publication_date, isbn=isbn)
