from django import forms
from .models import NewTestCase


class TestCaseForm(forms.ModelForm):    

    class Meta:
        model = NewTestCase
        fields = ('title', 'tag')
