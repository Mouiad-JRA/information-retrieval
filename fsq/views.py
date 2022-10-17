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
        model = BooleanModel("./data/*")
        results = model.query("book")
        print('results1')
        results = model.query("Dubai")
        print('results2')
        print(results)



# def handel(request):
#     return render(request, 'fsq/answer.html')
