from django.urls import path
from .views import search_medicaments

urlpatterns = [
    path('', search_medicaments, name='search_medicaments'),
]

