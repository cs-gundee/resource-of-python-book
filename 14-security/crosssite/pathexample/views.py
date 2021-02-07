from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, path):
    return HttpResponse(f"Таны хандсан зам: {path}")