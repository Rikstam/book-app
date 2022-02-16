from dataclasses import field
from django.forms.models import inlineformset_factory
from django import forms
from .models import Book
from .models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_pages',
            'rating'
        )
BookFormSet = inlineformset_factory(
    Author,
    Book,
    form=BookForm,
    min_num=2, # Min number of forms that must be filled
    extra=1, # Number of extra forms to display
    can_delete=False # Show a checkbox in each form to delete the row
)