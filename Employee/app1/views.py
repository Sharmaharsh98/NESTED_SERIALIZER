from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import generics

# Create your views here.

class EmployeeDetails(APIView):
    def get(self, request):
            emp = Employee.objects.all()
            if len(emp)== 0:
                msg = {"message": "employee details not found", "success":False, "Employee": []}
                return Response(msg, status= status.HTTP_200_OK)
            else:
                serializers = EmployeeSerializer(emp, many = True)
                return Response(serializers.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            #return HttpResponseRedirect(redirect_to ='http://127.0.0.1:8000/ad/')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EmployeeInfo(APIView):
    def get(self, request, regid):
        try:
            emp = Employee.objects.get(id=regid)
        except Employee.DoesNotExist:
            msg = { "message": "no employee found with this regid","success":False}
            return Response(msg, status= status.HTTP_200_OK)
        serializers = EmployeeSerializer(emp)
        return Response(serializers.data, status=status.HTTP_200_OK)
        

class Address(generics.ListCreateAPIView):
    queryset = AddressDetails.objects.all()
    serializer_class = AddressSerializer


class WorkExperience(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class QualificationInfo(generics.ListCreateAPIView):
    queryset = Qualifications.objects.all()
    serializer_class = QualificationSerializer


class ProjectInfo(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
