from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
    path('register/', registerFlightView, name='registerFlight')
    path('list/', listFlightView, name='listFlight')
    path('stats/', flightStatsView, name='flightStats')
]