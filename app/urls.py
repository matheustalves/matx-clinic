from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/<int:service_id>/',
         views.service_details, name='service_details'),
]
