from .models import Book, Profile
from django.forms import ModelForm, TextInput, SelectMultiple, Textarea, Select, DateInput, NumberInput, CharField, \
    ImageField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.fields['new_password2'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

    class Meta:
        model = User
        fields = ['username', 'password']


class CustomForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publishing_house', 'date', 'genre', 'language', 'isbn']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'author': SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'description': Textarea(attrs={
                'class': 'form-control'
            }),
            'publishing_house': Select(attrs={
                'class': 'form-control'
            }),
            'date': NumberInput(attrs={
                'class': 'form-control'
            }),
            'genre': Select(attrs={
                'class': 'form-control'
            }),
            'language': SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'isbn': NumberInput(attrs={
                'class': 'form-control'
            })
        }


class ProfileUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['familia', 'name', 'city', 'birth_date', 'lid', 'image']

        widgets = {
            'familia': TextInput(attrs={
                'class': 'form-control'
            }),
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'city': TextInput(attrs={
                'class': 'form-control'
            }),
            'birth_date': DateInput(attrs={
                'class': 'form-control'
            }),
            'lid': Textarea(attrs={
                'class': 'form-control'
            }),
        }
