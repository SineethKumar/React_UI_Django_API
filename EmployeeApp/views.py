from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department, Employee
from .serializer import SerializerDepartment, SerialozerEmployee
from django.core.files.storage import default_storage

# Create your views here.
@api_view(["GET"])
def dept_get(request):
    if request.method == "GET":
        departments = Department.objects.all()
        print(departments)
        serializer = SerializerDepartment(departments, many = True)
        print(serializer, serializer.data)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     data = request.data
    #     serializer = SerializerDepartment(data = data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response("Successfully added the data to database")
    #     return Response("Failed to add the data to database")
    # elif request.method == 'PUT':
    #     post = request.data
    #     serializer = SerializerDepartment(post, data = data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response("Updated the data successfully")
    #     return Response("Failed to update the data to database")
    # elif request.method == 'DELETE':
    #     data = Department.objects.get(departmentId = id)
    #     data.delete()
    #     return Response("Deleted the data successfully")
    else:
        return Response("please select the correct request")

@api_view(["GET"])
def emp_get(request):
    employees = Employee.objects.all()
    print(employees)
    serializer = SerialozerEmployee(employees, many = True)
    print(serializer, serializer.data)
    return Response(serializer.data)




@api_view(["POST"])
def dept_post(request):
    data = request.data
    serializer = SerializerDepartment(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response("Successfully added the data to database")
    return Response("Failed to add the data to database")

@api_view(["POST"])
def emp_post(request):
    data = request.data
    print(data)
    serializer = SerialozerEmployee(data=data)
    # print(serializer)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response("Successfully added the data to database")
    return Response("Failed to add the data to database")


    

@api_view(["PUT"])
def dept_put(request, id):
    data = request.data
    post = Department.objects.get(departmentId = id)
    serializer = SerializerDepartment(post, data = data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response("Updated the data successfully")
    return Response("Failed to update the data to database")

@api_view(["PUT"])
def emp_put(request, id):
    data = request.data
    post = Employee.objects.get(EmployeeId = id)
    serializer = SerialozerEmployee(post, data = data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response("Updated the data successfully")
    return Response("Failed to update the data to database")




@api_view(["DELETE"])
def dept_delete(request, id):
    data = Department.objects.get(departmentId = id)
    data.delete()
    return Response("Deleted the data successfully")

@api_view(["DELETE"])
def emp_delete(request, id):
    data = Employee.objects.get(EmployeeId = id)
    data.delete()
    return Response("Deleted the data successfully")




@api_view(["POST"])
def save_profile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return Response(file_name)