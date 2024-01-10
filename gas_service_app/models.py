from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

SERVICE_TYPES = (
        ('Cylinder did not arrived', 'Cylinder did not arrived'),
        ('Billing Related', 'Billing Related'),
        ('Others', 'Others'),    
    )

STATUS = (
        ('Submitted', 'Submitted'),
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved')
)

ROLES = (
    ('admin', 'admin'),
    ('customer', 'customer')
)

phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number should be of 10 digits."
)

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    def __str__(self):
        return f"Customer: {self.user}"


class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="service_request")
    request_type = models.CharField(max_length=100, choices=SERVICE_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default="Submitted")
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer}'s complaint"
    
    def save(self, *args, **kwargs):
        if self.status == "Submitted" or self.status == "Pending":
            self.resolved_at = None  # Set resolved_at to None if status is Submitted
        super().save(*args, **kwargs)

class Message(models.Model):
    related_to = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name="complaint_messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} : {self.related_to}"
