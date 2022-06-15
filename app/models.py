from django.db import models


class Device(models.Model):
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.FloatField()
    actual_price = models.FloatField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.manufacturer


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
