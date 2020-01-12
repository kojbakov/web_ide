from django import forms
from django.forms import formset_factory

from .models import NewTestCase

class TestCaseForm(forms.ModelForm):	

    class Meta:
	    model = NewTestCase
	    # fields = ('title', 'goals', 'tags', 'requirements', 'stage', 'pre_conditions', 'variants', 'steps',)
	    fields = ('title', 'requirements', 'tags', 'stage', 'goals', 'pre_conditions')
	    #ArticleFormSet = formset_factory(ArticleForm, extra=0)
