from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import *


class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30)
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput, min_length=8)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, min_length=8)
    age = forms.IntegerField(label='Введите свой возраст',
                             validators=[
                                 MinValueValidator(18, message="Вам должно быть не менее 18 лет"),
                                 MaxValueValidator(120, message="Возраст не может быть больше 120 лет"),
                             ],
                             min_value=18,
                             max_value=120,
                             widget=forms.TextInput(attrs={'maxlength': '3'})
                             )

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Вы должны быть старше 18')
        return age

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Buyer.objects.filter(name=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data
