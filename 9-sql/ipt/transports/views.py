from django.shortcuts import render
from .models import Center, Transport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "transports/index.html", {
        "transports": Transport.objects.all()
    })

def a_transport(request, transport_id):
    a_trans = Transport.objects.get(pk=transport_id)
    non_passengers = Passenger.objects.exclude(transports=a_trans).all()
    return render(request, "transports/a_transport.html", {
        "a_trans": a_trans,
        "passengers": a_trans.passengers.all(),
        "non_passengers": non_passengers
    })

def book(request, transport_id):

    # Хүсэлтийг шалгах
    if request.method == "POST":

        # Зорчих чиглэлд хандах
        transport = Transport.objects.get(pk=transport_id)
        
        # Өгөгдөл илгээсэн формоос зорчигчийн id -г олох
        passenger_id = int(request.POST["passenger"])

        # id -гаар нь зорчигчийг өгөгдлийн сангаас хайж олох
        passenger = Passenger.objects.get(pk=passenger_id)

        # Тухайн чиглэлд зорчигчийг нэмэх
        passenger.transports.add(transport)

        # Чиглэлийн дэлгэрэнгүй хуудас руу чиглүүлэх
        return HttpResponseRedirect(reverse("a_transport", args=(transport.id,)))