from django.contrib import admin


from .models import Faq, Problem, FaqAR, ProblemAR

admin.site.register(Faq)
admin.site.register(Problem)
admin.site.register(ProblemAR)
admin.site.register(FaqAR)
