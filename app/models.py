from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    insurance = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=50)
    scheduled_by = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
