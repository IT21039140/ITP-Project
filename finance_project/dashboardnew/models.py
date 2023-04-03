from django.db import models

# Create your models here.

CATEGORY=(
    ('Electricity','Electricity'),
    ('Water','Water'),
)

class utilitybill(models.Model):
    bill_id=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    date =models.DateField(max_length=100, null=True)
    price=models.FloatField(null=True)
class Meta:
    db_table="utilitybill"

class employee_salasry(models.Model):
    empid=models.CharField(max_length=20,null=True)
    basic_Salary=models.FloatField(null=True)
    OT_houres=models.PositiveIntegerField(null=True)
    OT_Rate=models.FloatField(null=True)
    deduction=models.FloatField(null=True)
    increment=models.FloatField(null=True)
    total_sal=models.FloatField(null=True)
    date =models.DateField(max_length=100, null=True)

    @property
    def netsal(self):
        self.total_sal=((self.basic_Salary*self.OT_Rate)/100.00)*float(self.OT_houres)+self.basic_Salary+(self.increment-self.deduction)
        return self.total_sal
    

class Meta:
    db_table="employee_salasry"


CATEGORY2 = (
    ('Womens', 'Womens' ),
    ('Mens', 'Mens' ),
    ('Kids', 'Kids' ),
)

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY2, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
class Meta:
    db_table="Item"

class fashion_order(models.Model):
    supplierId=models.PositiveIntegerField(null=True)
    ordermngrId=models.PositiveIntegerField(null=True)
    item_Id=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_order=models.PositiveIntegerField(null=True)
    orderDate=models.DateField(max_length=100,null=True)
    status=models.BooleanField(null=True)
    total_price=models.FloatField(null=True)
    ordermngrName=models.CharField(max_length=50,null=True)
    supplieName=models.CharField(max_length=50,null=True)

    @property
    def totalPrice(self):
        self.total_price=self.item_Id.price*self.quantity_order
        return self.total_price

class Meta:
    db_table="Item"


class sales(models.Model):
    Item_Id=models.ForeignKey(Item, on_delete=models.CASCADE)
    Item_name=models.CharField(max_length=50,null=True)
    Size=models.CharField(max_length=50,null=True)
    Price=models.FloatField(null=True)
    QTY=models.PositiveIntegerField(null=True)
    total_price=models.FloatField(null=True)
    position=models.CharField(max_length=50,null=True)
    salesdate=models.DateField(max_length=100,null=True)

    @property
    def totalPrice(self):
        self.total_price=self.Item_Id.price*self.QTY
        return self.total_price

class Meta:
    db_table="sales"