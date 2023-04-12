from django import forms
from django.forms import EmailInput, ModelForm, TextInput, Select, CheckboxInput, PasswordInput, DateInput
from .models import Todo, TodoItems
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'user': Select(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input form-control',
                'style': ' margin: 20%;',
            }),
            'deadline': DateInput(attrs={
                'class': 'form-date-input form-control',
                'style': ' margin: 20%;',
            }),
            'priority': Select(attrs={
                'class': 'form-select-input form-control',
                'style': ' margin: 20%;',
            }),
        }

class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItems
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'todo': Select(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input form-control',
                'style': ' margin: 20%;',
            }),
            'description': DateInput(attrs={
                'class': 'form-date-input form-control',
                'style': ' margin: 20%;',
            }),
        }

class EditTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_completed']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'width: 7%; margin: 20%;',
            }),
            'deadline': DateInput(attrs={
                'class': 'form-check-input',
                'style': 'width: 7%; margin: 20%;',
            }),
            'priority': Select(attrs={
                'class': 'form-check-input',
                'style': 'width: 7%; margin: 20%;',
            }),
        }


class UserCreation(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),

            'last_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
        }
