from django import forms
from django.test import TestCase

import datetime

from loans.forms import BookForm
from loans.models import Book


class BookFormTestCase(TestCase):
    # setUp is run automatically before each test'
    def setUp(self):
        self.form_input = {
            'authors': 'Doe. J',
            'title': 'A title',
            'publication_date': datetime.datetime(2024, 9, 1),
            'isbn': '123451990',
        }
        pass

    def test_form_has_necessary_fields(self):
        form = BookForm()
        self.assertIn('authors', form.fields)
        self.assertIn('title', form.fields)
        self.assertIn('publication_date', form.fields)
        self.assertIn('isbn', form.fields)

    # creates dictionary with form data and checks its validity
    def test_valid_form(self):
        form = BookForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    # creates dictionary with form data but a blank author, and makes sure this is not valid
    def test_blank_author_is_invalid(self):
        self.form_input['authors'] = ''
        form = BookForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # if author field is too long = invalid
    def test_overlong_author_is_invalid(self):
        self.form_input['authors'] = 'x' * 256
        form = BookForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # if title is blank = invalid
    def test_blank_title_is_invalid(self):
        self.form_input['title'] = ''
        form = BookForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # if title field is too long = invalid
    def test_overlong_title_is_invalid(self):
        self.form_input['title'] = 'x' * 256
        form = BookForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # non-date format = invalid
    def test_invalid_date_is_invalid(self):
        self.form_input['publication_date'] = 'this is not a date'
        form = BookForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # testing that adding a book to the aftercase works
    def test_valid_form_can_be_saved(self):
        form = BookForm(data=self.form_input)
        before_count = Book.objects.count()
        form.save()
        after_count = Book.objects.count()
        self.assertEqual(before_count+1, after_count)
