from django import forms
from django.forms import ModelForm

from fsq.models import Faq, Answer


class FaqForm(ModelForm):

    answer_text = forms.CharField(max_length=3000)

    class Meta:
        model = Faq
        fields = ['text', 'type']

    def save(self, commit=True):
        instance = super(FaqForm, self).save(commit=False)
        answer_text = self.cleaned_data['answer_text']
        text = self.cleaned_data['text']
        type = self.cleaned_data['type']
        instance.text = text
        instance.type = type
        if commit:
            instance.save()
            Answer.objects.create(text=answer_text, question=instance)
        return instance
