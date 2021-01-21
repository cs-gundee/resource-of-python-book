from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("<int:transport_id>", views.a_transport, name="a_transport"),
    path("<int:transport_id>/book", views.book, name="book"),
]