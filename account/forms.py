from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, label='Email-cím', help_text='Adj meg egy létező email címet')
    username = forms.CharField(max_length=30, label='Felhasználónév', help_text='Adj meg egy még nem létező nevet')

    class Meta:
        model = Account
        fields = ('email','username','password1','password2')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Jelszó',widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Hibás email vagy jelszó')
        
