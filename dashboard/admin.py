from django.contrib import admin
from .models import Product, Order,Supplier,Invoice

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity','price', 'category', 'comments','Supplier')
    list_filter = ('category','Supplier')
    search_fields = ('name', 'category', 'comments','Supplier')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'order_quantity', 'comments', 'order_datetime')
    list_filter = ('order_datetime','customer')
    search_fields = ('name_name', 'customer_username', 'comments')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Automatically update product quantity
        if obj.name:
            obj.name.quantity -= obj.order_quantity
            obj.name.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['name'].queryset = Product.objects.filter(quantity__gt=0)
        return form
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'name', 'contact_number', 'contact_email','description')
    # list_filter = ('category','Supplier')
    search_fields = ('company_name','name','contact_number')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('pdf_name', 'invoice_no', 'pdf_file','year','month')
    list_filter = ('year','month')
    search_fields = ('pdf_name','invoice_no','year','month')