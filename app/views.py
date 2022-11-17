from django.shortcuts import render, get_object_or_404
from .models import Customer, Service
from datetime import datetime
from .helpers import create_service


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
    if request.method == 'GET':
        search = ''

        if 's' in request.GET:
            search = request.GET['s']
            dt = datetime.strptime(search, '%Y-%m-%d')
            services = Service.objects.filter(
                date__date=dt).order_by('-date')[:10]
        else:
            services = Service.objects.order_by('-date')[:10]

        return render(request, 'app/services.html', {'services': services, 'search': search})

    elif request.method == 'POST':
        return create_service(request)

    elif request.method == 'PATCH':
        return create_service(request)

    elif request.method == 'DELETE':
        return create_service(request)

    return 'foo'


def service_details(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    return render(request, 'app/service-details.html', {'service': service})


def service_new(request):
    customers, search = [], ''

    if 's' in request.GET:
        search = request.GET['s']
        customers = Customer.objects.filter(
            name__contains=search).order_by('-created_at')

    return render(request, 'app/service-new.html', {'customers': customers, 'search': search})
