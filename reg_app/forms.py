from django import forms
from reg_app import models
from .models import Userdata
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'},),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'},),)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    city=forms.CharField(label='city')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'city'
        ]

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class Displayform(forms.Form):
    title=forms.CharField(label='Title',max_length=30)
    text= forms.CharField(widget=forms.Textarea(attrs={"rows":15, "cols":50}))


