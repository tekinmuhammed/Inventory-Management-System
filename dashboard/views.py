from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Order,Supplier,Invoice
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    cleaning_products = Product.objects.filter(category='Cleaning')
    count_list = cleaning_products.count()
    food = Product.objects.filter(category='Canteen')
    canteen =food.count()
    low_quantity_products = Product.objects.filter(quantity__lt=2,)
    Low_count =low_quantity_products.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
        'count_list':count_list,
        'canteen':canteen,
        'Low_count':Low_count
    }
    return render(request, 'dashboard/index.html', context)


# @login_required(login_url='user-login')
# def products(request):
#     product = Product.objects.all()
#     product_count = product.count()
#     customer = User.objects.filter(groups=2)
#     customer_count = customer.count()
#     order = Order.objects.all()
#     order_count = order.count()
#     product_quantity = Product.objects.filter(name='')
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             product_name = form.cleaned_data.get('name')
#             messages.success(request, f'{product_name} has been added')
#             return redirect('dashboard-products')
#     else:
#         form = ProductForm()
#     context = {
#         'product': product,
#         'form': form,
#         'customer_count': customer_count,
#         'product_count': product_count,
#         'order_count': order_count,
#     }
#     return render(request, 'dashboard/products.html', context)
@login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()# We can mannually change this category
    # product = Product.objects.filter(category='Stationary')# We can mannually change this category

    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()

    # Search functionality
    search_query = request.GET.get('search', '')  # Retrieve search query from the GET parameters
    if search_query:
        product = product.filter(name__icontains=search_query)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()

    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/products.html', context)

# Search funticion views 

@login_required(login_url='user-login')
def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/customers.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)


@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()

    context = {
        'order': order,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/order.html', context)

from django.shortcuts import render
from .models import Product

def low_quantity_products(request):
    # Filter products with quantity less than 2
    low_quantity_products = Product.objects.filter(quantity__lt=2,)#We can change this mannually by adding category

    context = {
        'low_quantity_products': low_quantity_products,
        'low_quantity_count': low_quantity_products.count(),
    }

    return render(request, 'dashboard/low_quantity_products.html', context)

def Food_products(request):
    # Filter products with category 'Food'
    food = Product.objects.filter(category='Canteen')
    # food = Product.objects.filter(category='Canteen',quantity__lt=2)

    context = {
        'food_products': food,
        'food_count': food.count(),
    }

    return render(request, 'dashboard/canteen_prodcut.html', context)


def clean_products(request):
    # Filter products with category 'Cleaning'
    cleaning_products = Product.objects.filter(category='Cleaning')
    # cleaning_products = Product.objects.filter(category='Cleaning',quantity__lt=2)


    context = {
        'cleaning_products': cleaning_products,
        'cleaning_count': cleaning_products.count(),
    }

    return render(request, 'dashboard/cleaning_prodcut.html', context)


# Supplier
def Supplie_list(request):
    # Filter products with category 'Food'
    supplier = Supplier.objects.all()
    # food = Product.objects.filter(category='Canteen',quantity__lt=2)

    context = {
        'Supplier_list': supplier,
        'Supplier_list_count': supplier.count(),
    }

    return render(request, 'dashboard/supplier_list.html', context)

def invoice_list(request):
    # Filter products with category 'Food'
    invoice = Invoice.objects.all()
    # food = Product.objects.filter(category='Canteen',quantity__lt=2)

    context = {
        'invoice_list': invoice,
        'invoice_list_count': invoice.count(),
    }

    return render(request, 'dashboard/invoice_list.html', context)