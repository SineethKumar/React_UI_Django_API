from .models import Department, Employee
from rest_framework import serializers

class SerializerDepartment(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SerialozerEmployee(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'