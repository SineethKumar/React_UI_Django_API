# Generated by Django 4.2.1 on 2023-05-06 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0003_alter_employee_employeeprofile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee", old_name="Department", new_name="DepartmentId",
        ),
    ]
