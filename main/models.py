from django.db import models
from django.contrib.auth.models import User
from .choices import TIPO_PRECIO_CHOICES, TIPO_CHOICES  # Importa los choices

class Categoria(models.Model):
    # Representa una categoría de productos, como 'Muebles', 'Juguetes', etc.
    nombre = models.CharField(max_length=100, unique=True)  # Nombre único de la categoría
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional para dar más detalles
    estado = models.BooleanField(default=True)  # Estado del producto (activo/inactivo)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Item(models.Model):
    codigo = models.CharField(max_length=100, unique=True)  # Código único para identificar el producto
    nombre = models.CharField(max_length=200)  # Nombre del producto
    descripcion = models.TextField()  # Descripción detallada del producto
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  # Tipo de producto (por ejemplo, 'Servicio', 'Producto')
    imagen = models.ImageField(upload_to='productos/images/', null=True, blank=True)  # Imagen del producto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')  # Categoría
    disponible = models.BooleanField(default=True)  # Disponibilidad
    estado = models.BooleanField(default=True)  # Estado activo/inactivo
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    actualizado_en = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    usuario_creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='productos_creados')  # Usuario creador
    usuario_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='productos_editados', blank=True)  # Usuario editor

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['nombre']

    def __str__(self):
        # Retorna el formato: 'Código - Tipo - Nombre'
        return f'{self.codigo} - {self.tipo} - {self.nombre}'



class Precio(models.Model):
    producto = models.ForeignKey(Item, related_name='precios', on_delete=models.CASCADE)  # Producto relacionado
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    tipo_precio = models.CharField(max_length=50, choices=TIPO_PRECIO_CHOICES)  # Tipo de precio
    activo = models.BooleanField(default=False)  # Indica si es el precio activo
    fecha_inicio = models.DateField(null=True, blank=True)  # Fecha de inicio
    fecha_fin = models.DateField(null=True, blank=True)  # Fecha de fin

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'
        ordering = ['producto', 'tipo_precio']
        constraints = [
            models.UniqueConstraint(fields=['producto', 'tipo_precio'], name='unique_precio_por_tipo')
        ]

    def __str__(self):
        return f'{self.producto.nombre} - {self.tipo_precio} - ${self.precio}'


class Banner(models.Model):
    # Representa un banner que puede aparecer en el sitio web, por ejemplo, en la página de inicio
    titulo = models.CharField(max_length=200)  # Título del banner
    descripcion = models.TextField()  # Descripción del paquete
    imagen = models.ImageField(upload_to='banners/', null=True, blank=True)  # Imagen opcional del banner
    url = models.URLField(max_length=500, null=True, blank=True)  # URL del banner (redirecciona cuando el usuario hace clic)
    activo = models.BooleanField(default=True)  # Estado del banner (activo/inactivo)
    estado = models.BooleanField(default=True)  # El estado del banner (activo/inactivo)
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación del banner
    actualizado_en = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    usuario_creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='banners_creados')  # Usuario creador
    usuario_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='banners_editados', blank=True)  # Usuario editor

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    # Información del cliente, vinculado a un usuario en el sistema
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el usuario de Django
    nombre = models.CharField(max_length=200)  # Nombre del cliente
    correo = models.EmailField(unique=True)  # Correo electrónico único del cliente
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Teléfono opcional del cliente
    direccion = models.TextField(blank=True, null=True)  # Dirección opcional del cliente
    registrado_en = models.DateTimeField(auto_now_add=True)  # Fecha y hora de registro
    estado = models.BooleanField(default=True)  # Estado del cliente (activo/inactivo)
    usuario_creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clientes_creados')  # Usuario creador
    usuario_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clientes_editados', blank=True)  # Usuario editor

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Paquete(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre del paquete
    descripcion = models.TextField()  # Descripción del paquete
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del paquete
    fecha_inicio = models.DateField(null=True, blank=True)  # Fecha de inicio del paquete
    fecha_fin = models.DateField(null=True, blank=True)  # Fecha de fin del paquete
    activo = models.BooleanField(default=True)  # Estado del paquete
    productos = models.ManyToManyField(Item, related_name='paquetes')  # Relación con productos (Item)

    class Meta:
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

