from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('nuevos_prod',views.nuevos_prod, name='nuevos_prod'),
    path('adopta',views.adopta, name='adopta'),
    path('registro',views.registro, name='registro'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('contacto',views.contacto, name='contacto'),
    path('socio',views.socio, name='socio'),
    path('productosAdd',views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>',views.productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),

    path('crud_categorias', views.crud_categorias, name='crud_categorias'),
    path('categoriasAdd',views.categoriasAdd, name='categoriasAdd'),
    path('categorias_del/<str:pk>',views.categorias_del, name='categorias_del'),
    path('categorias_edit/<str:pk>', views.categorias_edit, name='categorias_edit'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('ingresar_datos/', views.ingresar_datos, name='ingresar_datos'),
    path('limpiar_carrito/', views.limpiar_carrito, name='limpiar_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('procesar_datos/', views.procesar_datos, name='procesar_datos'),
    path('incrementar/<int:producto_id>/', views.incrementar_cantidad, name='incrementar_cantidad'),
    path('decrementar/<int:producto_id>/', views.decrementar_cantidad, name='decrementar_cantidad'),
    

    

    

]