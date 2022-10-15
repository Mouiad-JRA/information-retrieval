from django.views.generic.edit import CreateView

from .forms import FaqForm
from .models import Faq


class FaqCreateView(CreateView):
    form_class = FaqForm
    queryset = Faq.objects.all()
    template_name = 'fsq/faq.html'
    success_url = '/'
