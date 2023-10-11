from django import forms
from .models import Usluga, Review


class UslugaForm(forms.ModelForm):
    class Meta:
        model = Usluga
        fields = ['title', 'author', 'description', 'image', 'genre', 'cost']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)
