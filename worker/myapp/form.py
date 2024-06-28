from django import forms
from.models import Employee

class Emplyee(forms.ModelForm):
    model=Employee
    fields='__all__'