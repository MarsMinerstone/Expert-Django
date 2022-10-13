from django import forms
from .models import Mail


class ContactForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ("e_name", "email")

        widgets = {
        "e_name": forms.TextInput(attrs={"placeholder":"Имя", "data-form-field":"name", "class":"form-control", "id":"name-form4-q"}),
        "email": forms.EmailInput(attrs={"type":"email", "name":"from_email", "placeholder":"Email", "data-form-field":"email", "class":"form-control", "id":"email-form4-q"})
        }
