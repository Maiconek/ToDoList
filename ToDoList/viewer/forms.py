from django import forms
from django.forms import ModelForm, Select
from .models import *

class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = ['title', 'finished']