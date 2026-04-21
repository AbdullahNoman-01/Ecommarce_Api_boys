from rest_framework import serializers
from .import models


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    product = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Review
        fields = "__all__"