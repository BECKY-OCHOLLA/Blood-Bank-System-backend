from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Donor,BloodDonate 
from .serializer import DonorSerializer,BloodDonateSerializer
from rest_framework import status
from rest_framework.permissions import (SAFE_METHODS, AllowAny,IsAuthenticated)
import json
from collections import OrderedDict
from django.core import serializers
# from .renderers import UserJSONRenderer

                                       

# Create your views here.
class DonorList(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = DonorSerializer
   

    def get(self, request, format=None):
        all_donor = Donor.objects.all()
        serializers = DonorSerializer(all_donor, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = DonorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # To delete all stock
    def delete(self, request, format=None):
        all_bloodrequest = Donor.objects.all().delete()
        return Response({'message': 'Donor details were deleted successfully!'}, 
        status=status.HTTP_204_NO_CONTENT)
    
    # To update stock
    def put(self, request, format=None):
        serializer = DonorSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

    
class BloodDonateList(APIView):
    def get(self, request, format=None):
        all_donate = BloodDonate.objects.all()
        serializers = BloodDonateSerializer(all_donate, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers= BloodDonateSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        all_bloodrequest = BloodDonate.objects.all().delete()
        return Response({'message': 'Donor details were deleted successfully!'}, 
        status=status.HTTP_204_NO_CONTENT)
    
    # To update stock
    def put(self, request, format=None):
        serializer = BloodDonateSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

    