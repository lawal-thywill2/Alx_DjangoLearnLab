from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    # Optional: custom validation for title or description
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book title'
        })
    )
    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter book description'
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'description']

    def clean_title(self):
        # Example: prevent empty or unsafe titles
        title = self.cleaned_data.get('title')
        if '<script>' in title.lower():
            raise forms.ValidationError("Invalid characters in title")
        return title