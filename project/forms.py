from django import forms
from django.contrib.auth import get_user_model
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class ProjectForm(forms.ModelForm):
    edit_project = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    class Meta:
        model = models.Project
        fields = ['title', 'content']