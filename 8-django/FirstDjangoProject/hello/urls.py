from django.urls import path

from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:language>", views.greetings, name="greetings"),
    path("ru", views.byrussian, name="russian"),
    path("ch", views.bychinese, name="chinese"),
]