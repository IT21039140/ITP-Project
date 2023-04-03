from django.urls import path
from.import views

urlpatterns =[
    path('',views.indexSVD,name='dashboardnew-indexSVD'),
    path('employee/',views.employeeSVD,name='dashboardnew-employeeSVD'),
    path('employee/delete/<int:pk>',views.employee_deleteF,name='dashboardnew-employee_deleteF'),
    path('employee/update/<int:pk>',views.employee_updateF,name='dashboardnew-employee_updateF'),
    path('item/',views.itemSVD,name='dashboardnew-itemSVD'),
    path('order/',views.orderSVD,name='dashboardnew-orderSVD'),
    path('sales/',views.salesSVD,name='dashboardnew-salesSVD'),
    path('utility/',views.utilitySVD,name='dashboardnew-utilitySVD'),
    path('utility/delete/<int:pk>',views.utility_deleteF,name='dashboardnew-utility_deleteF'),
    path('utility/update/<int:pk>',views.utility_updateF,name='dashboardnew-utility_updateF'),
    path('report/',views.reportSVD,name='dashboardnew-reportSVD'),
    
]