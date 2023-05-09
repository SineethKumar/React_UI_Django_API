from django.db import models
# Create your models here.

class BaseClass(models.Model):
    created_by = models.DateField(auto_now_add=True)
    updated_by = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Department(BaseClass):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=30)

    def __str__(self):
        return self.departmentName+" "+str(self.departmentId)

class Employee(BaseClass):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=30)
    DepartmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    DateOfJoin = models.DateField()
    EmployeeProfile = models.CharField(max_length=200, null=True)