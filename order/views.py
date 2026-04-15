from django.shortcuts import render
from rest_framework import viewsets
from .import serializer
from .import models
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
   queryset = models.Order.objects.all()
   serializer_class = serializer.OrderSerializer