from . import models
from django import forms

class ProdForm(forms.ModelForm ):
    p_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product Name'}))
    p_desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Product Description'}))
    p_price = forms.IntegerField(widget=forms.NumberInput)
    

    class Meta:
        model=models.Product
        fields=['p_name','p_desc','p_price','p_image']