from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        field = '__all__'

  #  def create(self , validated_data):
  #     return Employee.objects.create(**validated_data)
    
  #  def update(self , employee , validated_data):
  #     newEmployee = Employee(**validated_data)
  #      newEmployee.id = employee.id 
  #      newEmployee.save()   
  #      return newEmployee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'
   