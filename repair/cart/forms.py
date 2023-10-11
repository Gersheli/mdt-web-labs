from django import forms

USLUGA_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddUslugaForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=USLUGA_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)