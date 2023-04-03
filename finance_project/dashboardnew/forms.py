from django import forms
from dashboardnew.models import employee_salasry
from dashboardnew.models import utilitybill
from dashboardnew.widget import DatePickerInput

class ExampleForm(forms.Form):
       date = forms.DateField(widget=DatePickerInput)

class employeesalForm(forms.ModelForm):
    class Meta:
        model=employee_salasry
        fields=[
            'empid',
            'basic_Salary',
            'OT_houres',
            'OT_Rate',
            'deduction',
            'increment',
            'date'
        ]
        widgets = {
            'date' : DatePickerInput(),
        }


class ExampleForm(forms.Form):
       date = forms.DateField(widget=DatePickerInput)

class utilitybillForm(forms.ModelForm):
    class Meta:
        model=utilitybill
        fields=[
            'bill_id',
            'category',
            'date',
            'price'
        ]
        widgets = {
            'date' : DatePickerInput(),
        }