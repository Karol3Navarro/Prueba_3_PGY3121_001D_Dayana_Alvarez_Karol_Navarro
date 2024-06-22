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
    path('productosAdd',views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>',views.productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),
]