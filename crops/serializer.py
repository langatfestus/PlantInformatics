from rest_framework import serializers
from .models import Crop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

# Path: crop_management/crops/views.py 
# Compare this snippet from crop_management/crops/models.py:
# from django.shortcuts import render