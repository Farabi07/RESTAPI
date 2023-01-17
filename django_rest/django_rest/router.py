from rest_framework.routers import DefaultRouter
from django_rest_app.viewsets import AdmissionViewSet

router = DefaultRouter()
router.register('admission', AdmissionViewSet)
