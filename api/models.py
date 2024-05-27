from django.db import models

class Categorias(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    padre_id = models.IntegerField(null=True)

class Marcas(models.Model):
    marca_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    sitio_web = models.CharField(max_length=255)

class Usuarios(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
    )
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=8, choices=ROLES)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

class Direcciones_envio(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50)
    calle = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=100)
    estado_provincia = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

class Productos(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marca_id = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=255)

class Pedidos(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )
    pedido_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    direccion_envio_id = models.ForeignKey(Direcciones_envio, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    fecha_entrega_estimada = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADOS)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago_id = models.IntegerField()  

class Detalles_pedido(models.Model):
    detalle_pedido_id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Formas_pago(models.Model):
    forma_pago_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    detalles = models.TextField()

class Carrito_compras(models.Model):
    carrito_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Metodos_pago_adicionales(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Transacciones(models.Model):
    transaccion_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_transaccion = models.DateTimeField()
    metodo_pago_id = models.ForeignKey(Metodos_pago_adicionales, on_delete=models.CASCADE)

class Valoraciones(models.Model):
    valoracion_id = models.AutoField(primary_key=True)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fecha_valoracion = models.DateTimeField()
