from django import forms
from django.forms import ModelForm
from .models import Customer, ServiceRequest, Message

class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = ('phone_number',)

        labels={
            'phone_number':"",
        }

        widgets ={
            'phone_number' : forms.TextInput(attrs={'placeholder': "Register your mobile number and",'cols': 50, 'rows': 1 ,'class': 'form-control'}),
        }

class ServiceRequestForm(ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('request_type', 'details', 'attachment', 'status')

        labels={
            'request_type' : "Complaint Type",
            'details' : 'Description',
            'attachment' : 'Attach your file here',
            'status' : 'Status'
        }

        widgets = {
            'request_type': forms.Select(attrs={'class': 'form-select'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class Messageform(ModelForm):
    class Meta:
        model = Message
        fields = ('content',)        

        labels = {
            'content': ""
        }

        widgets= {
            'content': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Message our customer support representative"})
        }