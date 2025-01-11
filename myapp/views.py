from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer , UserSerializer
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


#@api_view(['GET'])
#def root_view(request):
   # return Response({"message": "Welcome to the API root!"})

@api_view(['GET' , 'POST'])
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer( employees, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data , safe = False)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED )
        else: 
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
def employeeDetailView(request , pk):

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"} , status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee) 
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response({"message": "Employee deleted successfully"},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])   
def  UserListView(request):
    if request.method=='GET':
        users = User.objects.all()
    serializer = UserSerializer(users , many = True)
    return Response(serializer.data)
   

# Create your views here.
