from rest_framework import generics
from django.shortcuts import render
from .models import Churras
from .serializers import ChurrasSerializer


class ChurrasView(generics.ListCreateAPIView):
    queryset = Churras.objects.all().order_by('id')
    serializer_class = ChurrasSerializer


class ChurrasDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChurrasSerializer
    queryset = Churras.objects.all()
