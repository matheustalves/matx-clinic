from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customers/new/', views.customer_new, name='customer_new'),
    path('customers/<int:customer_id>/',
         views.customer_details, name='customer_details'),
    path('services/', views.services, name='services'),
    path('services/new/', views.service_new, name='service_new'),
    path('services/<int:service_id>/',
         views.service_details, name='service_details'),
]
