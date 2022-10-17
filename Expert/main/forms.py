from django import forms
from .models import Mail, Question


class ContactForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ("e_name", "email")

        widgets = {
        "e_name": forms.TextInput(attrs={"placeholder":"Имя", "data-form-field":"name", "class":"form-control", "id":"name-form4-q"}),
        "email": forms.EmailInput(attrs={"type":"email", "name":"from_email", "placeholder":"Email", "data-form-field":"email", "class":"form-control", "id":"email-form4-q"})
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("q_name", "q_email", "question")

        widgets = {
        "q_name": forms.TextInput(attrs={"type":"text", "name":"name", "placeholder":"Name", "data-form-field":"name", "class":"form-control", "id":"name-form5-u"}),
        "q_email": forms.EmailInput(attrs={"type":"email", "name":"email", "placeholder":"E-mail", "data-form-field":"email", "class":"form-control", "id":"email-form5-u"}),
        "question": forms.TextInput(attrs={"name":"textarea", "placeholder":"Message", "data-form-field":"textarea", "class":"form-control", "id":"textarea-form5-u"})
        }