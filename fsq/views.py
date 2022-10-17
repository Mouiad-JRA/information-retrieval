from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import FaqForm, ProblemForm
from .models import Faq, Problem


class FaqCreateView(CreateView):
    form_class = FaqForm
    queryset = Faq.objects.all()
    template_name = 'fsq/faq.html'
    success_url = '/'


class ProblemView(CreateView):
    form_class = ProblemForm
    queryset = Problem.objects.all()
    template_name = 'fsq/answer.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        pass


# def handel(request):
#     return render(request, 'fsq/answer.html')
