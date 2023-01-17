from rest_framework import viewsets
from .serializers import AdmissionSerializer
from .models import Admission


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
