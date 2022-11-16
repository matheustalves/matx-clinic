from django.shortcuts import render, get_object_or_404
from .models import Customer, Service
from datetime import datetime


def index(request):
    today_services = Service.objects.filter(
        date__date=datetime.today().date()).order_by('-date')[:10]

    return render(request, 'app/index.html', {'services': today_services})


def customers(request):
    return 'foo'


def customer_new(request):
    return 'foo'


def customer_details(request):
    return 'foo'


def services(request):
    return 'foo'


def service_details(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    return render(request, 'app/service-details.html', {'service': service})


def service_new(request):
    customers, query = [], ''

    if 's' in request.GET:
        query = request.GET['s']
        customers = Customer.objects.filter(
            name__contains=query).order_by('-created_at')

    return render(request, 'app/service-new.html', {'customers': customers, 'query': query})
