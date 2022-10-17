from django.urls import path

from .views import FaqCreateView, ProblemView

urlpatterns = [
    path('', FaqCreateView.as_view(), name='create'),
    path('ask', ProblemView.as_view(), name='answer'),
]