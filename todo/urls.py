from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("delete_todo", views.delete)
]
