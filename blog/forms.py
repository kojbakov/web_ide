from django import forms

from .models import NewTestCase

class TestCaseForm(forms.ModelForm):

    class Meta:
        model = NewTestCase
        # fields = ('title', 'goals', 'tags', 'requirements', 'stage', 'pre_conditions', 'variants', 'steps',)
        fields = ('title', 'requirements', 'tags', 'stage', 'goals', 'pre_conditions')