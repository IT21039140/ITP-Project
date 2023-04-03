from django.shortcuts import render,redirect
from django.http import HttpResponse
from dashboardnew.models import utilitybill
from dashboardnew.models import employee_salasry
from dashboardnew.models import Item
from dashboardnew.models import fashion_order
from dashboardnew.models import sales
from dashboardnew.forms import employeesalForm
from dashboardnew.forms import utilitybillForm

# Create your views here.
def indexSVD(request):
    return render(request,'dashboard/indexSVD.html')

def employeeSVD(request):
    sals = employee_salasry.objects.raw('SELECT * FROM dashboardnew_employee_salasry GROUP BY date ORDER BY date ASC ')
    
    if request.method=='POST':
        form=employeesalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardnew-employeeSVD')
    else:
        form=employeesalForm()
    
    employeedit={
        'sals':sals,
        'form':form,
    }
    return render(request,'dashboard/employeeSVD.html',employeedit)

def employee_deleteF(request,pk):
    employee=employee_salasry.objects.get(id=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('dashboardnew-employeeSVD')
    return render(request,'dashboard/employee_deleteF.html')

def employee_updateF(request,pk):
    employee=employee_salasry.objects.get(id=pk)
    if request.method=='POST':
        form=employeesalForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboardnew-employeeSVD')
    else:
       form=employeesalForm(instance=employee) 
    context={
        'form':form,
    }
    return render(request,'dashboard/employee_updateF.html',context)

def itemSVD(request):
    itemsF=Item.objects.all()
    itemdet={
        'itemsF':itemsF
    }
    return render(request,'dashboard/itemSVD.html',itemdet)

def orderSVD(request):
    ordersF=fashion_order.objects.all()
    orderdet={
        'ordersF':ordersF
    }
    return render(request,'dashboard/orderSVD.html',orderdet)


def salesSVD(request):
    salesF=sales.objects.all()
    salesdet={
        'salesF':salesF
    }
    return render(request,'dashboard/salesSVD.html',salesdet)

def utilitySVD(request):
    bills=utilitybill.objects.all()
    #bills=utilitybill.objects.raw('SELECT*FROM dashboardnew_utilitybill')

    if request.method=='POST':
        form=utilitybillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardnew-utilitySVD')
    else:
        form=utilitybillForm()
    
    utilbill={
        'bills':bills,
        'form':form
    }
    return render(request,'dashboard/utilitySVD.html',utilbill)

def utility_deleteF(request,pk):
    bill=utilitybill.objects.get(id=pk)
    if request.method=='POST':
        bill.delete()
        return redirect('dashboardnew-utilitySVD')
    return render(request,'dashboard/utility_deleteF.html')

def utility_updateF(request,pk):
    bill=utilitybill.objects.get(id=pk)
    if request.method=='POST':
        form=utilitybillForm(request.POST,instance=bill)
        if form.is_valid():
            form.save()
            return redirect('dashboardnew-utilitySVD')
    else:
       form=utilitybillForm(instance=bill)
     
    context={
        'form':form,
    }
    return render(request,'dashboard/utility_updateF.html',context)



def reportSVD(request):
    emprs=employee_salasry.objects.raw('SELECT * FROM dashboardnew_employee_salasry where MONTH(curdate())=MONTH(date)')

    context={
        'emprs':emprs
    }

    return render(request,'dashboard/reportSVD.html',context)


