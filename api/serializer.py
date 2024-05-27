from rest_framework import serializers
from .models import Categorias,Marcas,Usuarios,Direcciones_envio,Productos,Pedidos,Detalles_pedido,Formas_pago,Carrito_compras,Metodos_pago_adicionales,Transacciones,Valoraciones

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        

class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'
        
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class Direcciones_envioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones_envio
        fields = '__all__'
        
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'

class Detalles_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles_pedido
        fields = '__all__'

class Formas_pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formas_pago
        fields = '__all__'

class Carrito_comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito_compras
        fields = '__all__'

class Metodos_pago_adicionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodos_pago_adicionales
        fields = '__all__'

class TransaccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacciones
        fields = '__all__'

class ValoracionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoraciones
        fields = '__all__'
        
