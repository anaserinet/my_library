from django import forms

from .models import Book
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# Instead of using Form, we use model form becase since form and model code is very similar, this ensures we donr repeat code
#    class BookForm(forms.Form):
#    authors = forms.CharField(label="Authors", max_length=255)
#    title = forms.CharField(label="Title", max_length=255)
#    publication_date = forms.DateField(label="Publication date")
#    isbn = forms.CharField(label="ISBN", max_length=13)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'title', 'publication_date', 'isbn']
