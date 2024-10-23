from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('products/', views.products, name='dashboard-products'),
    path('Food_products/', views.Food_products, name='Food_products'),
    path('clean_products/', views.clean_products, name='clean_products'),
    path('low_quantity_products/', views.low_quantity_products, name='low_quantity_products'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
         name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
         name='dashboard-products-edit'),
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
    path('order/', views.order, name='dashboard-order'),
    path('Supplie_list/', views.Supplie_list, name='Supplie_list'),
    path('invoice_list/', views.invoice_list, name='invoice_list'),
    
    
]
