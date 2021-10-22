from django.urls import path
from django.contrib import admin
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    #path('detalle', views.detalle,name='detalle'),
    #path('carrito', views.carrito,name='carrito'),
    path('producto/<int:producto_id>/',  views.producto,name='producto'),
    path('categoria/<str:categoria_nombre>/', views.categoria,name='categoria'),

    #Acciones de carrito
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
    path('carrito',views.carrito,name='carrito'),
    path('eliminarProductoCarrito/<int:producto_id>',views.eliminarProductoCarrito,name="eliminarProductoCarrito"),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito')
]
