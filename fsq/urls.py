from django.urls import path

from .views import FaqCreateView, ProblemView, FaqARCreateView, ProblemARView

urlpatterns = [
    path('', FaqCreateView.as_view(), name='create_en'),
    path('ar', FaqARCreateView.as_view(), name='create_ar'),
    path('ask', ProblemView.as_view(), name='answer'),
    path('ask-ar', ProblemARView.as_view(), name='answer_ar'),
]