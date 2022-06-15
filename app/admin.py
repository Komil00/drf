from django.contrib import admin
from .models import Device,Client,Loan,LoadPayment
# Register your models here.

admin.site.register(Device)
admin.site.register(Client)
admin.site.register(Loan)
admin.site.register(LoadPayment)