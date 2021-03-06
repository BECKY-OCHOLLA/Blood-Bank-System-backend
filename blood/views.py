
from .models import Stock,BloodRequest
from .serializers import BloodRequestSerializer, StockSerializer
from django.shortcuts import render,HttpResponseRedirect
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404,HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = Stock.objects.all()
	if request.method == 'GET':
		serializer = StockSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

def get_data(request):
	data = BloodRequest.objects.all()
	if request.method == 'GET':
		serializer = BloodRequestSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)




class StockList(APIView):
      
      permission_classes = (AllowAny,)
      serializer_class = StockSerializer
    # To get all stock
      def get(self, request, format=None):
          all_stock = Stock.objects.all()
          serializers = StockSerializer(all_stock, many=True)
          return Response(serializers.data)
    
    # To post stock
      def post(self, request, format=None):
          serializers = StockSerializer(data=request.data)
          if serializers.is_valid():
              serializers.save()
              return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # To update stock
      def put(self, request, format=None):
        serializer = StockSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    # To delete all stock
      def delete(self, request, format=None):
        all_stock = Stock.objects.all().delete()
        return Response({'message': 'Stock lists were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

      


class BloodRequestList(APIView):
      permission_classes = (AllowAny,)
      serializer_class = BloodRequestSerializer
      
    
      def get(self, request, format=None):
          all_bloodrequest = BloodRequest.objects.all()
          serializers = BloodRequestSerializer(all_bloodrequest, many=True)
          return Response(serializers.data)
    
    
      def post(self, request, format=None):
          serializers = BloodRequestSerializer(data=request.data)
          if serializers.is_valid():
              serializers.save()
              return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
      def put(self, request, format=None):
        serializer = BloodRequestSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
      def delete(self, request, format=None):
        all_bloodrequest = BloodRequest.objects.all().delete()
        return Response({'message': 'Blood Request details were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

      

    
    
    
    
    