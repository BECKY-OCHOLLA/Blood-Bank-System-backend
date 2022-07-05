# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import BloodRequest, Stock 

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('bloodgroup', 'unit')
        
        
