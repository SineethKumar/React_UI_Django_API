# Generated by Django 4.2.1 on 2023-05-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="EmployeeProfile",
            field=models.ImageField(blank=True, null=True, upload_to="profiles/"),
        ),
    ]