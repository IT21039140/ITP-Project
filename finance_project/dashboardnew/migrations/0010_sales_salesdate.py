# Generated by Django 4.1.1 on 2022-09-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardnew', '0009_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='salesdate',
            field=models.DateField(max_length=100, null=True),
        ),
    ]
