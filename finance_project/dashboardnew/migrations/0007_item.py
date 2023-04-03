# Generated by Django 4.1.1 on 2022-09-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardnew', '0006_employee_salasry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Womens', 'Womens'), ('Mens', 'Mens'), ('Kids', 'Kids')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
