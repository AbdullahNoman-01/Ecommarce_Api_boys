from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer
# Create your views here.



class CartViewSet(viewsets.ModelViewSet):
   queryset = models.Cart.objects.all()
   serializer_class = serializer.CartSerializer