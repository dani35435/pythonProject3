from django import forms

from .models import Product


class OrderCreate(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'photo_file')
        enctype = "multipart/form-data"