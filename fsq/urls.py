from django.urls import path

from .views import FaqCreateView

urlpatterns = [
    path('', FaqCreateView.as_view(), name='create'),
]