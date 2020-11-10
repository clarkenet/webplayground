from django import forms
from .models import Page


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput({'class': 'form-control', 'placeholder': 'Título'}),
            'content': forms.Textarea({'class': 'form-control'}),
            'order': forms.NumberInput({'class': 'form-control'})
        }
        labels = {
            'title': '', 'content': '', 'order': ''
        }
