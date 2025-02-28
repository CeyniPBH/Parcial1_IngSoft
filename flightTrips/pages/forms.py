from django import forms
from .models import Flight

# Formulario para registrar los vuelos
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'flightType', 'price']
        widgets = {
            'flightType': forms.Select(choices=Flight.FLIGHT_TYPES)
        }


