from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label="User name:", max_length=20)
    password = forms.CharField(label="Password:", max_length=20)