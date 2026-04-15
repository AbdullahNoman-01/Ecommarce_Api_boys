from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer

class ReviewViewSet(viewsets.ModelViewSet):
   queryset = models.Review.objects.all()
   serializer_class = serializer.ReviewSerializer