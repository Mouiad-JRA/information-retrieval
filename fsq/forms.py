from django import forms
from django.forms import ModelForm

from fsq.models import Faq, Problem


class FaqForm(ModelForm):

    class Meta:
        model = Faq
        fields = ['question', 'answer', 'type']


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['question', 'type']
