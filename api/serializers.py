from rest_framework import serializers
from .models import Churras


class ChurrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Churras
        fields = '__all__'
