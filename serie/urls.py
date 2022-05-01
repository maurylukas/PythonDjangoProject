
from django.urls import path, include
from .views import Homepage, Homeseries, Details

app_name = 'serie'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('series/', Homeseries.as_view(), name='homeseries'),
    path('series/<int:pk>', Details.as_view(), name='details'),
]