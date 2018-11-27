from django.urls import path

from . import views

app_name = 'species'

urlpatterns = [
    path('a/',
         views.tree,
         name='Tree'),
]