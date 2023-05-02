from django.urls import path

from . import views

urlpatterns = [
    path("webhook/", views.handle_webhook, name="handle_webhook"),
]
