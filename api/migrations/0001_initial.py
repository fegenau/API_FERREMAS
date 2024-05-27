# Generated by Django 5.0.6 on 2024-05-08 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('padre_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direcciones_envio',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=255)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=100)),
                ('estado_provincia', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Formas_pago',
            fields=[
                ('forma_pago_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('detalles', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('marca_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('sitio_web', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Metodos_pago_adicionales',
            fields=[
                ('metodo_pago_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente'), ('empleado', 'Empleado')], max_length=8)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField()),
                ('fecha_entrega_estimada', models.DateTimeField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('procesando', 'Procesando'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_pago_id', models.IntegerField()),
                ('direccion_envio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.direcciones_envio')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('imagen', models.CharField(max_length=255)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorias')),
                ('marca_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.marcas')),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_pedido',
            fields=[
                ('detalle_pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pedidos')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('transaccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_transaccion', models.DateTimeField()),
                ('metodo_pago_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metodos_pago_adicionales')),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pedidos')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='direcciones_envio',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.CreateModel(
            name='Carrito_compras',
            fields=[
                ('carrito_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Valoraciones',
            fields=[
                ('valoracion_id', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('fecha_valoracion', models.DateTimeField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
    ]