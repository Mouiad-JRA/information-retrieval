import re
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .boolean_model import BooleanModel
from .forms import FaqForm, ProblemForm
from .models import Faq, Problem
from .preprocessing import handler
from .vector_model import vector_space


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
                results = vector_space("./data/*", question)
                print("results")
                print(results)
                print('Vector Model results')

            for question_id in results:
                faq = Faq.objects.filter(pk=question_id[0:-4]).first()
                string = faq.answer
                q = question.lower().replace('and', '')
                q = q.replace('or', '')
                q = q.replace('()', '')
                q = q.replace('(', '')
                q = q.replace(')', '')
                for index in q.split(' '):
                    if index != "":
                        s = string.split()
                        for i in range(len(s)):
                            if index.lower() in s[i].lower():
                                result = f"<b><span>{s[i].capitalize()}</span></b>"
                                s[i] = result
                        list_to_str = ' '.join([str(elem) for elem in s])
                        string = list_to_str
                        # result = f"<b><span class='words' style='color:red;'>{index.capitalize()}</span></b>"
                        # string = re.sub(index, result, string.lower(), re.IGNORECASE)

                print('momo')
                print(string)
                small_response.update({string: faq.question})
            response.update({'empty': True})
            if small_response:
                response.update({'empty': False})
                response.update({'Result': small_response})

            return render(request, 'fsq/answer.html', response)

        except:
            raise ValidationError("Please check")

# https://github.com/abuwildanm/Information-Retrieval/blob/master/scraping.py
