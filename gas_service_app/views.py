from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from .decorators import unauth_user, allowed_users
from django.contrib.auth.models import Group
from django import forms
from django.http import JsonResponse
import json

#forms
from .forms import Customerform, ServiceRequestForm, Messageform

#Models
from .models import Customer, ServiceRequest, User, Message

# Create your views here.

@unauth_user
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "gas_service_app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            customer_group, created = Group.objects.get_or_create(name='customer')
            user = User.objects.create_user(username, email, password)
            user.save()
            user.groups.add(customer_group)
        except IntegrityError:
            return render(request, "gas_service_app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("first:index"))
    else:
        return render(request, "gas_service_app/register.html")

@unauth_user
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("first:index"))
        else:
            return render(request, "gas_service_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "gas_service_app/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("first:login"))

@login_required(login_url='first:login')
@allowed_users(allowed_roles=['customer'])
def index(request):
    all_customers = Customer.objects.all()
    form = ServiceRequestForm()
    # check if user is already a customer
    is_registered = any(customer.user == request.user for customer in all_customers)

    
    
    form.fields['status'].widget = forms.HiddenInput()
    return render(request, 'gas_service_app/index.html', {
        'customerForm': Customerform(),
        'submit_request' : form,
        'all_customer': all_customers,
        'is_registered': is_registered  
    })

#Registering Customer with phone number
@login_required(login_url='first:login')
@allowed_users(allowed_roles=['customer'])
def customer(request):
    print(request)
    if request.method == "POST":
            form = Customerform(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.phone_number = form.cleaned_data["phone_number"]
                form.save()
                messages.add_message(request, messages.SUCCESS, "Customer Registered Successfully")
                return redirect('first:index')
                #Value Error issued has not been solved

#Saving Customer's Complaint
@login_required(login_url='first:login')
@allowed_users(allowed_roles=['customer'])
def submit_request(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        files = request.FILES.get('attachment')
        #print("files------>", files)
        data = json.loads(json.dumps(request.POST))
        x = ServiceRequest(customer=customer, request_type=data["request_type"], details = data["details"], attachment=files) 
        x.save()
        messages.add_message(request, messages.SUCCESS, "Your compliant has been registered successfully")
        return redirect("first:index")

    return JsonResponse({'error': 'Invalid request method'})

@login_required(login_url="first:login")
@allowed_users(allowed_roles=['customer'])
def submitted_requests(request):
    try:
        customer = Customer.objects.get(user=request.user)
        track = ServiceRequest.objects.filter(customer=customer, status="Submitted").order_by('-submitted_at')
        return render(request, 'gas_service_app/track_requests.html', {
            'requests' : track
        })
    except:
        return HttpResponse("Register your phone number") 

@login_required(login_url="first:login")
@allowed_users(allowed_roles=['customer'])
def view_request(request, pk):                   
    view_request = ServiceRequest.objects.get(pk=pk)
    messages = Message.objects.filter(related_to=pk).order_by('-timestamp')
    return render(request, "gas_service_app/view_request.html", {
        "request" : view_request,
        "message_form" : Messageform,
        "all_messages_related_to_complaint" : messages
    })

@login_required(login_url="first:login")
@allowed_users(allowed_roles=['customer'])
def resolved(request):
    # print("Resolved")
    try:
        user = Customer.objects.get(user=request.user)
        resolved = ServiceRequest.objects.filter(customer=user, status="Resolved")
        # print("Resolved 2")
        return render(request, "gas_service_app/resolved.html", {
            'resolved' : resolved
    })
    except:
        return HttpResponse("Register your phone number")

@login_required(login_url="first:login")
@allowed_users(allowed_roles=['customer'])
def reopen_request(request, pk):
    get_service = ServiceRequest.objects.get(id=pk)
    get_service.status = "Submitted"
    get_service.save()
    # print(get_service.status) 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def message_csr(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        # print("data---------->",data)
        related_to = ServiceRequest.objects.get(id=pk)
        sender = request.user
        content = data['message']
        timestamp = timezone.now()
        x = Message(related_to=related_to, sender=sender, content=content, timestamp=timestamp)
        x.save()
        return JsonResponse({"message" : "success"})
