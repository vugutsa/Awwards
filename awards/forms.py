from django import forms
from .models import Projects

class NewProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['pub_date']