from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core import validators


class webform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "name", "password", "phone_number"]

    def save(self, commit=True):
        user = super(webform, self).save(commit=False)
        password = self.cleaned_data["password"]
        print(len(password))
        if len(password) != 0:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
