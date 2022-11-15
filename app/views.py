from django.shortcuts import render, get_object_or_404
from .models import Customer, Service
from datetime import datetime


def index(request):
    today_services = Service.objects.filter(
        date__date=datetime.today().date()).order_by('-date')[:10]

    return render(request, 'app/index.html', {'services': today_services})


def service_details(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    return render(request, 'app/service-details.html', {'service': service})
