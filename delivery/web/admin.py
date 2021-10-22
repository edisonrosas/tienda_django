from django.contrib import admin
from .models import Categoria,Producto
# Register your models here.

#Para ingresar al admin
#user: admin
#passowrd. admin
class ProductoAdmin(admin.ModelAdmin):

    class Meta: 
        model = Producto
  
    list_display = ['nombre','categoria','stock','precio']  

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)