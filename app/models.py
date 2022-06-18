from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Device(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturer', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='model', on_delete=models.CASCADE)
    price = models.FloatField()
    actual_price = models.FloatField()
    is_active = models.BooleanField()


class Client(models.Model):
    fullname = models.CharField(max_length=35)
    birthdate = models.DateField()
    passport = models.CharField(max_length=35)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname


class Loan(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    payed = models.FloatField()
    first_pay = models.FloatField()
    end_date = models.DateTimeField()
    month_pay = models.FloatField()
    # def __str__(self):
    #     return self.client


class LoadPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.FloatField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    state = models.CharField(max_length=50)
