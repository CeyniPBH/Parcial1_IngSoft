from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index')
    path('register/', registerFlightView, name='registerFlight')
    path('list/', listFlightView, name='listFlight')
    path('stats/', flightStatsView, name='flightStats')
]