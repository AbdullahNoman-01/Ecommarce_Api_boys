from rest_framework import serializers
from .import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

class SummarSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(many=False)
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.SummarCollection
        fields = "__all__"