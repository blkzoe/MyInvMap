"""
Definition of forms.
"""

from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _




class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Enter password'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm password'}))


    class Meta:
        model = User
        fields = {'username','email'}

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")

        return confirm_password

class ProductForm(forms.ModelForm):    
    name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Name'}))
    description = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Description'}))
    price = forms.IntegerField(widget = forms.NumberInput(attrs = {'placeholder': 'price'}))
    
    class Meta:
        model = Product
        fields = {'name','description','price'}
     



