from django import forms
from django.core.exceptions import ValidationError
from requests import request
from core.models import *

class Application_forms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Комментарии к заказу'})


    class Meta:
        model = Application
        fields = ['number_cab', 'description']


class ApplicationFormEdit(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['number_cab', 'description']