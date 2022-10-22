from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from fsq.models import Faq, Problem, FaqAR, ProblemAR


class FaqForm(ModelForm):
    class Meta:
        model = Faq
        fields = ['question', 'answer', 'type']


class FaqARForm(ModelForm):
    class Meta:
        model = FaqAR
        fields = ['question', 'answer', 'type']


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['question', 'type']

    def __init__(self, *args, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"

    def clean_type(self):
        type = self.cleaned_data['type']
        if not type:
            raise ValidationError("Please Choose an algorithm type")
        return type

    def clean_question(self):
        question = self.cleaned_data['question']
        if not question:
            raise ValidationError("Please Enter a Question")
        return question


class ProblemARForm(forms.ModelForm):
    class Meta:
        model = ProblemAR
        fields = ['question', 'type']

    def __init__(self, *args, **kwargs):
        super(ProblemARForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"

    def clean_type(self):
        type = self.cleaned_data['type']
        if not type:
            raise ValidationError("Please Choose an algorithm type")
        return type

    def clean_question(self):
        question = self.cleaned_data['question']
        if not question:
            raise ValidationError("Please Enter a Question")
        return question