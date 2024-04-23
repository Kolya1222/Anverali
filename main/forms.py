from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import User

class Loginform(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                
                'class':'input-box',
                'placeholder':'Логин'
            }
        ), label=''
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'label':'',
                'class':'input-box',
                'placeholder':'Пароль'
            }
        ), label=''
    )

class Registerform(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'input-box',
                'placeholder':'Логин'
            }
        ), label=''
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'input-box',
                'placeholder':'Пароль'
            }
        ), label=''
    ) 
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'input-box',
                'placeholder':'Пароль'
            }
        ), label=''
    ) 
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'input-box',
                'placeholder':'Почта'
            }
        ), label=''
    ) 
    aboutme = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'input-box1',
                'placeholder':'О себе'
            }
        ), label=''
    ) 
    Metric_name: forms.Select(attrs={'class': 'input-box'})
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email','Metric_name','aboutme')

