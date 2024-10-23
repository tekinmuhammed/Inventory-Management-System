from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Canteen', 'Canteen'),
    ('Cleaning', 'Cleaning'),
    ('Food', 'Food'),
    ('Medical Item', 'Medical Item'),
    ('Saftey Item', 'Saftey Item')
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    comments = models.CharField(max_length=100, null=True)
    Supplier = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'
    # we will do this latter

    # def calculate_total_price(self):
    #     if self.quantity is not None and self.price is not None:
    #         return self.quantity * self.price
    #     return None


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    comments = models.CharField(max_length=100, null=True)
    order_datetime = models.DateTimeField(default=None, blank=True, null=True)

    def _str_(self):  # Corrected method name
        return f'{self.customer}-{self.name.name}' if self.name else f'{self.customer}-No Product'

    # def save(self, *args, **kwargs):
    #     super(Order, self).save(*args, **kwargs)
    #     # Automatically update product quantity
    #     if self.name:
    #         self.name.quantity -= self.order_quantity
    #         self.name.save()
class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField()
    description = models.CharField(max_length=220)

    def _str_(self):
        return self.company_name
    


# To save pdf file 
    
class Invoice(models.Model):
    pdf_name = models.CharField(max_length=255,)
    invoice_no = models.CharField(max_length=255, unique=True)
    pdf_file = models.FileField(upload_to='invoice_pdfs/')
    year = models.IntegerField(default=None, blank=True, null=True)
    month = models.IntegerField(default=None, blank=True, null=True)

    def _str_(self):
        return self.pdf_name    
        