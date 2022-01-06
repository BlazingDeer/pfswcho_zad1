from rest_framework import viewsets
from .models import FibSeq
from .serializers import FibSeqSerializer

# Create your views here.


class FibSeqViewSet(viewsets.ModelViewSet):
    queryset = FibSeq.objects.all().order_by("-id")[:10]
    serializer_class = FibSeqSerializer
