from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField, \
    PasswordChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Имя пользователя')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтвердите пароль')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', )
    new_password1 = forms.CharField(label='Новый пароль')
    new_password2 = forms.CharField(label='Подтвердите новый пароль')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class CustomSettingsUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Логин/Никнейм')
    first_name = forms.CharField(required=False, max_length=15, label='Имя')
    last_name = forms.CharField(required=False, max_length=20, label='Фамилия')
    phone = forms.CharField(required=False, min_length=11, max_length=11, label='Телефонный номер')
    email = forms.EmailField(required=False, label='E-Mail')
    country = forms.CharField(required=False, max_length=15, label='Страна')
    region_area = forms.CharField(required=False, max_length=30, label='Регион / Область')
    city = forms.CharField(required=False, max_length=15, label='Город')
    address1 = forms.CharField(required=False, max_length=65, label='Адрес')
    address2 = forms.CharField(required=False, max_length=65, label='Дополнительный адрес')
    index = forms.CharField(required=False, max_length=10, label='Индекс')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'country', 'region_area', 'city', 'address1',
                  'address2', 'index']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=15, label="Имя ⃰")
    phone = forms.CharField(required=False, min_length=11, max_length=11, label="Номер Телефона")
    email = forms.EmailField(label="Почта ⃰")
    message = forms.CharField(max_length=400, label="Сообщение ⃰")

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Имя не должно начинаться с цифры')
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\D', phone):
            raise ValidationError('Номер должен соответствовать формату "8 (499) 123-45-67"')
        return phone

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
        self.fields['message'].widget = forms.Textarea(
            attrs={'class': 'form-control', 'rows': '13', 'placeholder': self.fields['message'].label})
