from dashboardnew.models import employee_salasry
from dashboardnew.models import utilitybill
from dashboardnew.models import fashion_order
from dashboardnew.models import sales

def report1(request):
    utilir=utilitybill.objects.raw('SELECT * FROM dashboardnew_utilitybill where MONTH(curdate())=MONTH(date)')
    
    return {'utilir':utilir}

def report2(request):
    ordersr=fashion_order.objects.raw('SELECT * FROM dashboardnew_fashion_order where MONTH(curdate())=MONTH(orderDate)')
    
    return {'ordersr':ordersr}

def report3(request):
    salesr=sales.objects.raw('SELECT * FROM dashboardnew_sales where MONTH(curdate())=MONTH(salesdate)')
    
    return {'salesr':salesr}

def total1(request):
    emps=employee_salasry.objects.raw('SELECT * FROM dashboardnew_employee_salasry where MONTH(curdate())=MONTH(date)')
    total1=0
    for i in emps:
        total1=total1+i.netsal
    
    return {'total1':total1}

def total2(request):
    ordersr=fashion_order.objects.raw('SELECT * FROM dashboardnew_fashion_order where MONTH(curdate())=MONTH(orderDate)')
    
    total2=0
    for i in ordersr:
        total2=total2+i.totalPrice
    
    return {'total2':total2}

def total3(request):
    salesr=sales.objects.raw('SELECT * FROM dashboardnew_sales where MONTH(curdate())=MONTH(salesdate)')
    
    total3=0
    for i in salesr:
        total3=total3+i.totalPrice
    
    return {'total3':total3}

def total4(request):
    utilir=utilitybill.objects.raw('SELECT * FROM dashboardnew_utilitybill where MONTH(curdate())=MONTH(date)')
    
    total4=0
    for i in utilir:
        total4=total4+i.price
    
    return {'total4':total4}