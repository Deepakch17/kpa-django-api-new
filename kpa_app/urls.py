from django.urls import path
from .views import KPAFormCreateView, KPAFormDetailView

urlpatterns = [
    path('api/form-data/', KPAFormCreateView.as_view()),
    path('api/form-data/<int:pk>/', KPAFormDetailView.as_view()),
]
