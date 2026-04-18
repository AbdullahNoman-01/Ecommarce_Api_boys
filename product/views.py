from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
   queryset = models.Product.objects.all()
   serializer_class = serializer.ProductSerializer

class SummarViewSet(viewsets.ModelViewSet):
   queryset = models.SummarCollection.objects.all()
   serializer_class = serializer.SummarSerializer