from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('nuevos_prod',views.nuevos_prod, name='nuevos_prod'),
    path('adopta',views.adopta, name='adopta'),
    path('registro',views.registro, name='registro'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('bandana',views.bandana, name='bandana'),
    path('correa',views.correa, name='correa'),
    path('identificacion',views.identificacion, name='identificacion'),
    path('contacto',views.contacto, name='contacto'),
    path('carrito',views.carrito, name='carrito'),
    path('socio',views.socio, name='socio'),

]