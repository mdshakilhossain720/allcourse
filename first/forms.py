from typing import Any
from django import forms

class StudnetRegestion(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    batch=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput())
    repassword=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        clean_data=super().clean()
        valname=self.cleaned_data['first_name']
        valemail=self.cleaned_data['email']
        password=self.changed_data['password']
        repassword=self.changed_data['repassword']

        if password !=repassword:
             raise forms.ValidationError('Match not match')
    
        if len(valname)<4:
            raise forms.ValidationError('enter the vale name')
        

        if len(valemail)<10:
            raise forms.ValidationError('enter the emil')
        





    def clean_name(self):
        valname=self.cleaned_data['first_name']
        if len(valname)<4:
            raise forms.ValidationError('enter the name')
        return valname
    
