from django.urls import path

from . import views
app_name = 'species'

urlpatterns = [
    path('<int:pk>',
         views.TreeDetail.as_view(),
         name='TreeDetail'),
    path('',
         views.TreeList.as_view(),
         name='TreeList'),
    path('a/',
         views.tree,
         name='Tree'),
]