from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory

from .models import NewTestCase
from .models import MyModel
from .models import StepsResults
from .models import Case
from .models import Steps


#from .models import User

'''
class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )
BookFormset = formset_factory(BookForm, extra=1)



BookModelFormset = modelformset_factory(
    BookForm,
    fields=('name', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    }
)
'''

class TestCaseForm(forms.ModelForm):    

    class Meta:
        model = NewTestCase
        # fields = ('title', 'goals', 'tags', 'requirements', 'stage', 'pre_conditions', 'variants', 'steps',)
        # fields = ('title', 'requirements', 'tags', 'stage', 'goals', 'pre_conditions', 'step_name')
        fields = ('title', 'tags')
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

'''
StepsResultsFormset = modelformset_factory(
    StepsResults,
    fields=('test_case', 'step', 'result'),
    extra=1,
)
'''

'''

class TestCaseForm(forms.ModelForm):

    class Meta:
        model = NewTestCase
        fields = ('title', 'steps')



        #return form_class



BookModelFormset = modelformset_factory(NewTestCase, fields=('title', 'steps'), extra=1)

class MyForm(forms.Form):

    title = forms.CharField()
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()
    class Meta:
        fields = ('title', 'extra_fields')
'''
"""
BookModelFormset = modelformset_factory(
    NewTestCase,
    fields=('title', 'step_name'),
    extra=1,
    widgets={'step_name': forms.TextInput(attrs={
            'class': 'form-control'
        })}
    )
"""

