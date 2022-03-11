# coding=utf-8
from .models import Records
from django.forms import ModelForm, TextInput, EmailInput, DateTimeInput


class RecordsForm(ModelForm):
    class Meta:
        model = Records
        fields = ['email', 'name_user', 'surname_user', 'date']

        widgets = {
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "name_user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "surname_user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата записи'
            }),
        }

        it = iter(widgets)
