"""
rango URL Configuration
"""

from django.urls import path

# to create an initial mapping of views in rango
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]
