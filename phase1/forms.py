from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    secret_code = forms.CharField(max_length=100, required=True, help_text='Enter the secret code to sign up.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'secret_code')
