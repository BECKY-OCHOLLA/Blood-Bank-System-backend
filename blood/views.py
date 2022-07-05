
from .models import Stock,BloodRequest
from .serializers import BloodRequestSerializer, StockSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser 



class StockList(APIView):
      
      permission_classes = (AllowAny,)
      serializer_class = StockSerializer
    # To get all stock
      def get(self, request, format=None):
          all_stock = Stock.objects.all()
          serializers = StockSerializer(all_stock, many=True)
          return Response(serializers.data)
    
    
      

    
    
    
    
    