from django.contrib import admin
from .models import Categorias,Marcas,Usuarios,Direcciones_envio,Productos,Pedidos,Detalles_pedido,Formas_pago,Carrito_compras,Metodos_pago_adicionales,Transacciones,Valoraciones

# Register your models here.
admin.site.register(Categorias),
admin.site.register(Marcas),
admin.site.register(Productos),
admin.site.register(Usuarios),
admin.site.register(Direcciones_envio),
admin.site.register(Pedidos),
admin.site.register(Detalles_pedido),
admin.site.register(Formas_pago),
admin.site.register(Carrito_compras),
admin.site.register(Metodos_pago_adicionales),
admin.site.register(Transacciones), 
admin.site.register(Valoraciones)
