from django.urls import path

from . import views
app_name = 'species'

urlpatterns = [
    path('treea/',
         views.TreeList.as_view()),
    path('treed/',
         views.TreeDetail.as_view()),
    path('', views.tree, name='Tree'),
]