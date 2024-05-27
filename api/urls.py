from django.urls import path,include
from rest_framework import routers
from api import views



router =  routers.DefaultRouter()
router.register(r'categoria',views.CategoriasViewSet),
router.register(r'marcas',views.MarcasViewSet),
router.register(r'usuarios',views.UsuariosViewSet),
router.register(r'direcciones_envio',views.Direcciones_envioViewSet),
router.register(r'productos',views.ProductosViewSet),
router.register(r'pedidos',views.PedidosViewSet),
router.register(r'detalles_pedido',views.Detalles_pedidoViewSet),
router.register(r'formas_pago',views.Formas_pagoViewSet),
router.register(r'carrito_compras',views.Carrito_comprasViewSet),
router.register(r'metodos_pago_adicionales',views.Metodos_pago_adicionalesViewSet),
router.register(r'transacciones',views.TransaccionesViewSet),
router.register(r'valoraciones',views.ValoracionesViewSet),


urlpatterns = [
    path('', include(router.urls)), 
]
