from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Categorias, Marcas, Usuarios
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json
from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient


class IntegrationTests(APITestCase):
    def setUp(self):
        # Crear un usuario para autenticar las peticiones
        self.user = User.objects.create_user(username='testuser', password='testpass')
        #self.token = Token.objects.create(user=self.user)
        #self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Datos de prueba
        self.categoria_data = {'nombre': 'Electrónica', 'descripcion': 'Dispositivos electrónicos'}
        self.marca_data = {'nombre': 'Apple', 'descripcion': 'Tecnología y dispositivos', 'sitio_web': 'https://www.apple.com'}

    def test_create_and_get_categoria(self):
        # Crear una categoría
        url = reverse('categorias-list')
        response = self.client.post(url, self.categoria_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Obtener la categoría creada
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], self.categoria_data['nombre'])

    def test_create_and_get_marca(self):
        # Crear una marca
        url = reverse('marcas-list')
        response = self.client.post(url, self.marca_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Obtener la marca creada
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], self.marca_data['nombre'])

    def test_create_usuario_and_order_flow(self):
        # Crear un usuario
        usuario_data = {
            'nombre': 'John Doe', 
            'correo_electronico': 'john.doe@example.com', 
            'contrasena': 'password123', 
            'rol': 'cliente', 
            'direccion': '123 Main St', 
            'telefono': '1234567890'
        }
        url = reverse('usuarios-list')
        response = self.client.post(url, usuario_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Crear una categoría
        categoria_url = reverse('categorias-list')
        self.client.post(categoria_url, self.categoria_data, format='json')

        # Crear una marca
        marca_url = reverse('marcas-list')
        self.client.post(marca_url, self.marca_data, format='json')

        # Crear un producto usando la categoría y marca creadas
        producto_data = {
            'nombre': 'iPhone',
            'descripcion': 'Smartphone de Apple',
            'precio': '999.99',
            'costo': '500.00',
            'stock': 10,
            'categoria_id': Categorias.objects.first().pk,
            'marca_id': Marcas.objects.first().pk,
            'imagen': 'https://example.com/iphone.jpg'
        }
        url = reverse('productos-list')
        response = self.client.post(url, producto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Crear un pedido
        pedido_data = {
            'usuario_id': Usuarios.objects.first().pk,
            'direccion_envio_id': 1,  # Asume que tienes una dirección de envío creada en setUp
            'fecha_pedido': '2023-12-01T00:00:00Z',
            'fecha_entrega_estimada': '2023-12-10T00:00:00Z',
            'estado': 'pendiente',
            'total': '999.99',
            'forma_pago_id': 1  # Asume que tienes una forma de pago creada en setUp
        }
        url = reverse('pedidos-list')
        response = self.client.post(url, pedido_data, format='json')
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Obtener el pedido creado
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(len(response.data), 1)
        
#Test MERCADOPAGO
        
#class MercadoPagoIntegrationTests(TestCase):
#    def setUp(self):
#        self.client = APIClient()
#        self.create_preference_url = reverse('create_preference')  # Asegúrate de que el nombre del URL esté correcto
#        self.notification_url = reverse('payment_notification')  # Asegúrate de que el nombre del URL esté correcto
#
#    @patch('mercadopago.SDK.preference')
#    def test_create_preference(self, mock_preference):
#        # Configurar el mock para la respuesta de Mercado Pago
#        mock_preference().create.return_value = {
#            "response": {
#                "id": "12345",
#                "init_point": "https://www.mercadopago.com.ar/checkout/v1/redirect?pref_id=12345",
#                # Otros campos necesarios...
#            }
#        }
#
#        data = {
#            "title": "Test Item",
#            "quantity": 1,
#            "price": 100.0,
#            "email": "test@example.com"
#        }
#        
#        response = self.client.post(self.create_preference_url, data, format='json')
#        
#        self.assertEqual(response.status_code, 200)
#        self.assertIn("id", response.data)
#        self.assertIn("init_point", response.data)
#        # Agregar otras aserciones según sea necesario
#
#    def test_payment_notification(self):
#        notification_data = {
#            "data": {
#                "id": "12345"
#            }
#        }
#        
#        response = self.client.post(self.notification_url, notification_data, format='json')
#        
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(response.data, {"status": "received"})
#        # Agregar otras aserciones según sea necesario

