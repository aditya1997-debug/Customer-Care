from django.urls import path

from . import views

app_name = "first"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("customer", views.customer, name="customer"),
    path("submit_request", views.submit_request, name="submit_request"), #done with javaScript
    path("submitted_requests", views.submitted_requests, name="request_tracking"), 
    path("view_request/<int:pk>", views.view_request, name="view_request"),
    path("resolved_requests", views.resolved, name="resolved"),
    path("message_csr/<int:pk>", views.message_csr, name="message_csr"),
    path("reopen_request/<int:pk>", views.reopen_request, name="reopen")
]
