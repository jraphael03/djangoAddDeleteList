from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["fname", "lname", "age"]
        labels = {"fname": "First Name", "lname": "Last Name"}
