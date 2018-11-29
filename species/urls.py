from django.urls import path

from . import views

app_name = 'species'

urlpatterns = [
    path('', views.tree, name='Tree'),
    path('autocomplete/', views.autocomplete,  name='Autocomplete'),
    path('search/', views.search,  name='Search'),
]