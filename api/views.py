from rest_framework import viewsets, permissions
from .serializer import CategoriaSerializer, MarcasSerializer, UsuariosSerializer, Direcciones_envioSerializer, ProductosSerializer, PedidosSerializer, Detalles_pedidoSerializer, Formas_pagoSerializer, Carrito_comprasSerializer, Metodos_pago_adicionalesSerializer, TransaccionesSerializer, ValoracionesSerializer

from .models import Categorias, Marcas, Usuarios, Direcciones_envio, Productos, Pedidos, Detalles_pedido, Formas_pago, Carrito_compras, Metodos_pago_adicionales, Transacciones, Valoraciones
import mercadopago 
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = CategoriaSerializer


class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class Direcciones_envioViewSet(viewsets.ModelViewSet):
    queryset = Direcciones_envio.objects.all()
    serializer_class = Direcciones_envioSerializer


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class Detalles_pedidoViewSet(viewsets.ModelViewSet):
    queryset = Detalles_pedido.objects.all()
    serializer_class = Detalles_pedidoSerializer


class Formas_pagoViewSet(viewsets.ModelViewSet):
    queryset = Formas_pago.objects.all()
    serializer_class = Formas_pagoSerializer


class Carrito_comprasViewSet(viewsets.ModelViewSet):
    queryset = Carrito_compras.objects.all()
    serializer_class = Carrito_comprasSerializer


class Metodos_pago_adicionalesViewSet(viewsets.ModelViewSet):
    queryset = Metodos_pago_adicionales.objects.all()
    serializer_class = Metodos_pago_adicionalesSerializer


class TransaccionesViewSet(viewsets.ModelViewSet):
    queryset = Transacciones.objects.all()
    serializer_class = TransaccionesSerializer


class ValoracionesViewSet(viewsets.ModelViewSet):
    queryset = Valoraciones.objects.all()
    serializer_class = ValoracionesSerializer


class CreatePreferenceView(APIView):
    def post(self, request):
        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
        preference_data = {
            "items": [
                {
                    "title": request.data.get("title"),
                    "quantity": int(request.data.get("quantity")),
                    "currency_id": "ARS",
                    "unit_price": float(request.data.get("price"))
                }
            ],
            "payer": {
                "email": request.data.get("email")
            },
            "back_urls": {
                "success": "",
                "failure": "",
                "pending": ""
            },
            "auto_return": "approved",
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        return Response(preference)
    
class PaymentNotificationView(APIView):
    def post(self, request):
        # Procesar la notificación recibida
        payment_id = request.data.get("data", {}).get("id")
        if payment_id:
            # Aquí puedes actualizar el estado del pago en tu base de datos
            pass
        return Response({"status": "received"}, status=200)