from django import forms
from products.models import Product

class AddToBasketForms(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput)
    quantity = forms.IntegerField(max_value=5)

    def save(self, basket):
        basket.add(
            self.cleaned_data('product'),
            self.cleaned_data('quantity')
        )
        return basket
