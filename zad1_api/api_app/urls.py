from django.urls import path
from .views import FibSeqViewSet
from rest_framework.routers import SimpleRouter

app_name = "api_app"

router = SimpleRouter()
router.register("fibseq", FibSeqViewSet, basename="fibseq")

urlpatterns = router.urls
