from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import Http404
from .models import Categoria, Producto
from web.carrito import Cart

# Create your views here.

def index(request):
    #Cargar productos
    product_list=Producto.objects.order_by('nombre')[:6]
    #Cargar categorias
    category_list=Categoria.objects.order_by('nombre')

    #Valores de carrito / Icono funcional
    CarritoProducto = Cart(request)
    NumProdsCart=CarritoProducto.totalprods
    PriceCart=format(CarritoProducto.totalprice,'.2f')

    context = {'product_list':product_list,'category_list':category_list,'ProdsCart':NumProdsCart,'PriceCart':PriceCart}
    return render(request,'index.html', context)

def producto(request,producto_id):
    producto=get_object_or_404(Producto,pk=producto_id)

    #Valores de carrito
    NumProdsCart=request.session.get("totalProds")
    PriceCart=format(request.session.get("totalPrice"),'.2f')
    return render (request, 'detalle.html', {'product':producto,'ProdsCart':NumProdsCart,'PriceCart':PriceCart})

def categoria(request,categoria_nombre):
    categoria_obj=get_object_or_404(Categoria,nombre=categoria_nombre)
    product_list=get_list_or_404(Producto,categoria=categoria_obj)
    category_list=Categoria.objects.order_by('nombre')

    #Valores de carrito
    NumProdsCart=request.session.get("totalProds")
    PriceCart=format(request.session.get("totalPrice"),'.2f')

    return render (request, 'index.html', {'product_list':product_list,'category_list':category_list,'ProdsCart':NumProdsCart,'PriceCart':PriceCart})


#acciones de ShopCart
def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    #Valores de carrito
    NumProdsCart=request.session.get("totalProds")
    PriceCart=format(request.session.get("totalPrice"),'.2f')

    return render(request,'carrito.html',{'ProdsCart':NumProdsCart,'PriceCart':PriceCart})

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))

    #Valores de carrito
    NumProdsCart=request.session.get("totalProds")
    PriceCart=format(request.session.get("totalPrice"),'.2f')

    return render(request,'carrito.html',{'ProdsCart':NumProdsCart,'PriceCart':PriceCart})

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    #Valores de carrito
    NumProdsCart=request.session.get("totalProds")
    PriceCart=format(request.session.get("totalPrice"),'.2f')
    return render(request,'carrito.html',{'ProdsCart':NumProdsCart,'PriceCart':PriceCart})

def carrito(request):
    print(request.session.get("cart"))
    #Valores de carrito
    NumProdsCart=request.session.get("totalProds")
    PriceCart=format(request.session.get("totalPrice"),'.2f')
    return render(request,'carrito.html',{'ProdsCart':NumProdsCart,'PriceCart':PriceCart})
    