import json

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .boolean_model import BooleanModel
from .forms import FaqForm, ProblemForm
from .models import Faq, Problem
from .preprocessing import handler


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
        handler(Faq.objects.all(), 'data')
        try:
            question = self.request.POST.get('question')
            algorthim_type = self.request.POST.get('type')
            results = []
            response = {}
            small_response = {}
            if algorthim_type == '0':
                model = BooleanModel("./data/*")
                results = model.query(question)
                print('BooleanModel results')
                print(results)
            elif algorthim_type == '1':
                model = BooleanModel("./data/*")
                results = model.query(question)
                print('Extended BooleanModel results')
                print(results)
            elif algorthim_type == '2':
                model = BooleanModel("./data/*")
                results = model.query(question)
                print('Vector Model results')

                print(results)
            for question_id in results:
                faq = Faq.objects.filter(pk=question_id[0:-4]).first()
                small_response.update({faq.answer: faq.question})
            response.update({'empty': True})
            if small_response:
                response.update({'empty': False})
                response.update({'Result': small_response})
            print(response)
            return render(request, 'fsq/answer.html', response)
        except:
            raise ValidationError("Please check")

# def handel(request):
#     return render(request, 'fsq/answer.html')
