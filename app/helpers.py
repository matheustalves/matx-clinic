from django.shortcuts import redirect
from .models import Customer, Service
from datetime import datetime


def create_service(request):
    obj = request.POST

    date = datetime.strptime(
        f'{obj["date"]} {obj["time"]}', '%Y-%m-%d %H:%M')

    service = Service(
        customer=Customer.objects.get(id=obj['customer']),
        type=obj['type'],
        date=date,
        status=obj['status'],
        scheduled_by=obj['scheduled_by'],
        info=obj['info'],
    )

    service.save()

    return redirect('/')
