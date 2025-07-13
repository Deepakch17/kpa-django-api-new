from rest_framework import generics
from .models import KPAFormData
from .serializers import KPAFormDataSerializer

class KPAFormCreateView(generics.CreateAPIView):
    queryset = KPAFormData.objects.all()
    serializer_class = KPAFormDataSerializer

class KPAFormDetailView(generics.RetrieveAPIView):
    queryset = KPAFormData.objects.all()
    serializer_class = KPAFormDataSerializer