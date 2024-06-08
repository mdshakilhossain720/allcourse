from django.core import validators
from.models import Student
from django import forms


class StudentRegestion(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','roll','course','email','password']
        