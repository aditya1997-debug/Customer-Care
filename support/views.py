from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from gas_service_app.models import ServiceRequest
from gas_service_app.forms import ServiceRequestForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .decorators import allowed_users, unauth_user
from django.contrib.auth.decorators import login_required
from gas_service_app.models import Message
from django.contrib.auth.models import Group
from gas_service_app.forms import Messageform
from gas_service_app.models import User
from django.db.models import Q
from django import forms
import json
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
            return render(request, "support/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            support_group, created = Group.objects.get_or_create(name='support')
            user = User.objects.create_user(username, email, password)
            user.save()
            user.groups.add(support_group)
        except IntegrityError:
            return render(request, "support/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("support:index"))
    else:
        return render(request, "support/register.html")

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
            return HttpResponseRedirect(reverse("support:index"))
        else:
            return render(request, "support/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "support/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("support:login"))

@login_required(login_url="support:login")
@allowed_users(allowed_roles=['support'])
def index(request):
    requests = ServiceRequest.objects.filter(Q(status="Submitted") | Q(status="Pending")).order_by('-submitted_at')
    return render(request, "support/index.html", {
        'requests' : requests
    })

@login_required(login_url="support:login")
@allowed_users(allowed_roles=['support'])
def edit_request(request, pk):
    service = get_object_or_404(ServiceRequest, pk=pk)
    attachment = service.attachment
    # # print(service.request_type)
    # # print(service.customer.id, service.customer.user.id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service)
        if form.is_valid():
            instance = form.save(commit=False)  
            instance.request_type = service.request_type
            instance.details = service.details
            instance.resolved_at = timezone.now()  
            instance.status = form.cleaned_data["status"]
            instance.save()  
            return redirect('support:index')
        else:
            return HttpResponse(form.errors)
    else:  
        form = ServiceRequestForm(instance=service)
        form.fields['request_type'].widget = forms.HiddenInput()
        form.fields['details'].widget.attrs['readonly'] = True
        form.fields['attachment'].widget = forms.HiddenInput()

    return render(request, "support/edit_request.html", { 
        'form' : form,
        'service' : service,
        'attachment' : attachment,
        'message_form' : Messageform(),
        'all_messages_related_to_complaint' : Message.objects.filter(related_to=service).order_by('-timestamp')
    })

@login_required(login_url="support:login")
@allowed_users(allowed_roles=['support'])
def resolved(request):
    resolved = ServiceRequest.objects.filter(status="Resolved")
    return render(request, "support/resolved.html", {
        'resolved' : resolved
})


def message_csr(request, pk):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            #print("data---------->",data)
            related_to = ServiceRequest.objects.get(id=pk)
            sender = request.user
            content = data['message']
            timestamp = timezone.now()
            x = Message(related_to=related_to, sender=sender, content=content, timestamp=timestamp)
            x.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponse("Error 404")
