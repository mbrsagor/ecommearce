from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Transaction_Form(forms.Form):
    name = forms.ModelChoiceField(queryset = Item.objects.all())
    quantity = forms.IntegerField()



class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
