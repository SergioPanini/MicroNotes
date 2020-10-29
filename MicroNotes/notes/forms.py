from django import forms

class RegisterForm(forms.Form):

    name = forms.CharField(max_length=256, required=False)
    password = forms.CharField(max_length=256, required=False)

class CreateNote(forms.Form):
    title = forms.CharField(max_length=256)
    text = forms.CharField(max_length=256)