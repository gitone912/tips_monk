from django import forms
from django.forms import TextInput
from .models import *

class user_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(user_status, self).__init__(*args, **kargs)
    class Meta:
        model = quest
        fields = ['ques']
        widgets = {
            'ques': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'enter your question'
                }),
        }
        