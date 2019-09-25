from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class EmployeeListAPIView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

class EmployeeAPIView(generics.ListAPIView):
    queryset          =Employee.objects.all()
    serializer_class  =EmployeeSerializer
