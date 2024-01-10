from django.contrib import admin
from .models import Customer, ServiceRequest, Message

# Register your models here.

admin.site.register(Customer)
admin.site.register(ServiceRequest)
admin.site.register(Message)
