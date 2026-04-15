from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer
# Create your views here.


class SerializerViewSet(viewsets.ModelViewSet):
   queryset = models.Payment.objects.all()
   serializer_class = serializer.PaymentSerializer