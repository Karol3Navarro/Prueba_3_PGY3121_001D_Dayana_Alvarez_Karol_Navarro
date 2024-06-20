from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('nuevos_prod',views.nuevos_prod, name='nuevos_prod'),
]