from django.urls import path
from . import views

app_name = "support"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # path("view_request/<int:pk>", views.view_request, name="view_request"),
    path("edit_request/<int:pk>", views.edit_request, name="edit_request"),
    path("message_csr/<int:pk>", views.message_csr, name="message_csr"),
    path("resolved_requests", views.resolved, name="resolved")
]
