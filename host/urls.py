from django.urls import path
from . import views

app_name = 'host'
urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('all/', views.all, name='all'),
    path('live/', views.live, name='live'),
    path('past/', views.past, name='past'),
]
