from django import forms
from .models import Projects,Profile

class NewProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['pub_date']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 
                