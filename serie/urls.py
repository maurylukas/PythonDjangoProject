
from django.urls import path, include
from .views import Homepage, Homeseries, Details, Search

app_name = 'serie'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('series/', Homeseries.as_view(), name='homeseries'),
    path('series/<int:pk>', Details.as_view(), name='details'),
    path('search/', Search.as_view(), name='search'),
]