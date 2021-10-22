
class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
        #Contador de productos    
        totalprods=self.session.get("totalProds")
        if not totalprods:
            totalprods = self.session["totalProds"] = 0
        self.totalprods=totalprods
        #Suma Total
        totalprice=self.session.get("totalPrice")
        if not totalprice:
            totalprice = self.session["totalPrice"] = 0
        
        self.totalprice=totalprice

    def add(self,producto,qty):
        self.totalprods+=int(qty)
        if str(producto.id) not in self.cart.keys():  
            self.totalprice+=float(qty * producto.precio) 
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre" : producto.nombre,
                "cantidad" : qty,
                "precio": str(producto.precio),
                "imagen" : producto.imagen.url,
                "total" : str(format(qty * producto.precio,'.2f'))
                }          
        else:
            for key,value in self.cart.items():
                if key == str(producto.id):
                    self.totalprice += qty* float(value["precio"]) 
                    value["cantidad"] = str(int(value["cantidad"]) + qty)
                    value["total"] = str(format(float(value["cantidad"]) * float(value["precio"]),'.2f'))                             
                    break
  
        self.save()
        
    def save(self):
        self.session["cart"] = self.cart
        self.session["totalProds"]=self.totalprods
        self.session["totalPrice"]=self.totalprice
        self.session.modified = True
        
    def remove(self,producto):
        
        for key,value in self.cart.items():
            if key == str(producto.id):
                self.totalprice-= float(value["total"])
                self.totalprods-= int(value["cantidad"])

        producto_id = str(producto.id)          
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
            
    def clear(self):
        self.session["cart"] = {}
        self.session["totalProds"]=0
        self.session["totalPrice"]=0
        self.totalprods=0
