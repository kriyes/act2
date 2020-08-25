from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField()
    # password2 = forms.CharField()
    # role = forms.intergerField()


    class Meta(UserCreationForm):
        model = User
        fields = ('username','email','password')
