from django import forms

class register_form(forms.Form):

    name = forms.CharField(max_length=256, required=False)
    password = forms.CharField(max_length=256, required=False)