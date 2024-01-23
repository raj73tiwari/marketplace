from . import models
from django import forms

class Prod_form(forms.ModelForm ):
    class Meta:
        model=models.Product
        fields=['p_name','p_desc','p_price','p_image']