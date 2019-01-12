from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class CreateUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Username'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password'}
        )
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password Confirmation'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Last Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'First Name'})
    )

    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()

        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if not password or password != password_confirmation:
            raise forms.ValidationError(_('Both passwords are not equals'))

        return cleaned_data
