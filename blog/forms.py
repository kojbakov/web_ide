from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory

from .models import NewTestCase
from .models import StepsResults
from .models import Case
from .models import Steps



class TestCaseForm(forms.ModelForm):    

    class Meta:
        model = NewTestCase
        # fields = ('title', 'goals', 'tags', 'requirements', 'stage', 'pre_conditions', 'variants', 'steps',)
        # fields = ('title', 'requirements', 'tags', 'stage', 'goals', 'pre_conditions', 'step_name')
        fields = ('title',)
        #ArticleFormSet = formset_factory(ArticleForm, extra=0)

class StepsForm(forms.ModelForm):    

    class Meta:
        model = StepsResults
        # fields = ('title', 'goals', 'tags', 'requirements', 'stage', 'pre_conditions', 'variants', 'steps',)
        # fields = ('title', 'requirements', 'tags', 'stage', 'goals', 'pre_conditions', 'step_name')
        fields = ('step', 'result')
        #ArticleFormSet = formset_factory(ArticleForm, extra=0)

class TestCase(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('title', 'tags',)

class Steps(forms.ModelForm):

    class Meta:
        model = Steps
        fields = ('step', 'result',)


