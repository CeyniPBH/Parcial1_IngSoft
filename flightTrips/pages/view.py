from django.shortcuts import render, redirect
from .models import Flight
from .forms import FlightForm

def home(request):
    return render(request, 'home.html')

def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
def list_flight(request):
    flights = Flight.objects.order.by('price')
    return render(request, 'list_flight.html', {'flights': flights})


def flight_stats(request):
    national_count = Flight.objects.filter(flightType='NAC').count()
    international_count = Flight.objects.filter(flightType='INT').count()
    national_agv_price = Flight.objects.filter(flightType='NAC').aggregate(Avg('price'))
    return render(request, 'flight_stats.html', {

        'national_count': national_count,
        'international_count': international_count,
        'national_agv_price': national_agv_price
    })