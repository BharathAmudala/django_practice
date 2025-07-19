from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        db_table = 'Product'

class Stock(models.Model):
    name = models.CharField(max_length=250)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'Stock'

class Purchase(models.Model):
    Product = models.ForeignKey(Product, db_column='Product_id', on_delete = models.CASCADE)
    quantity_purchased = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    date =  models.DateTimeField()

    class Meta:
        db_table = 'Purchase'

class Sale(models.Model):
    Product = models.ForeignKey(Product, db_column='Product_id', on_delete = models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

    class Meta:
        db_table = 'Sale'