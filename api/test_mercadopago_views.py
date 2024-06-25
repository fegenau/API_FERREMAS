import json
from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class MercadoPagoIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_preference_url = reverse('create_preference')  # Asegúrate de que el nombre del URL esté correcto
        self.notification_url = reverse('payment_notification')  # Asegúrate de que el nombre del URL esté correcto

    @patch('mercadopago.SDK.preference')
    def test_create_preference(self, mock_preference):
        # Configurar el mock para la respuesta de Mercado Pago
        mock_preference().create.return_value = {
            "response": {
                "id": "12345",
                "init_point": "https://www.mercadopago.com.ar/checkout/v1/redirect?pref_id=12345",
                # Otros campos necesarios...
            }
        }

        data = {
            "title": "Test Item",
            "quantity": 1,
            "price": 100.0,
            "email": "test@example.com"
        }
        
        response = self.client.post(self.create_preference_url, data, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.data)
        self.assertIn("init_point", response.data)
        # Agregar otras aserciones según sea necesario

    def test_payment_notification(self):
        notification_data = {
            "data": {
                "id": "12345"
            }
        }
        
        response = self.client.post(self.notification_url, notification_data, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "received"})
        # Agregar otras aserciones según sea necesario
