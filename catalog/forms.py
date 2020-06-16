from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, help_text='Feel free enter your feedback')

    def clean_message(self):
        data = self.cleaned_data['message']
        if len(data) > 3:
            raise ValidationError('Invalid - too long')
        return data


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'