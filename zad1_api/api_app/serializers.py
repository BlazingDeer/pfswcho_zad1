from rest_framework import serializers
from .models import FibSeq


class FibSeqSerializer(serializers.HyperlinkedModelSerializer):
    result = serializers.IntegerField(read_only=True)

    class Meta:
        model = FibSeq
        fields = ["number", "result"]
