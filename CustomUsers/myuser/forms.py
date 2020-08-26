from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    displayname = forms.CharField(max_length=80)
    homepage = forms.URLField(required=False)
    age = forms.IntegerField(required=False)
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
