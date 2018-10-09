from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields = ('title', 'text', 'ololo', 'tags')
        fields = ('title', 'goals', 'tags', 'requirements', 'stage', 'pre_conditions', 'variants', 'steps',)