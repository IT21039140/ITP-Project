# Generated by Django 4.1.1 on 2022-09-29 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardnew', '0010_sales_salesdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_salasry',
            old_name='basicSal',
            new_name='basic_Salary',
        ),
    ]
