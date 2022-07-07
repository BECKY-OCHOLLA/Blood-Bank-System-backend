from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
# from .models import  Patient
from registrations.models import  Patient
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly
from .serializer import PatientSerializer
from rest_framework import status

# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from django.http import Http404,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def get_data(request):
	data = Patient.objects.all()
	if request.method == 'GET':
		serializer = PatientSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)




def profile(request):
    current_user = request.user
    patient = Patient.objects.filter(user_id=current_user.pk).first()
    return render(request,{"patient":patient})

class PatientList(APIView):
    def get (self,request, format=None):
        all_patient = Patient.objects.all()
        serializers = PatientSerializer(all_patient,many=True)
        return Response (serializers.data)
        
    def post(self,request,format=None):
        serializers = PatientSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)    
        
    def delete(self, request, format=None):
        all_patient = Patient.objects.all().delete()
        return Response({'message': 'Donor details were deleted successfully!'}, 
        status=status.HTTP_204_NO_CONTENT)
        
    def put(self, request, format=None):
        serializer = PatientSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
