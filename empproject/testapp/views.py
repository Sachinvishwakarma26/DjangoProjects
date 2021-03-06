from django.shortcuts import render
from testapp.models import Employee
from rest_framework import viewsets
from testapp.serializers import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
