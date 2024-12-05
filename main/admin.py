from django.contrib import admin
from image_uploader_widget.admin import ImageUploaderInline
from image_uploader_widget.widgets import ImageUploaderWidget

from .choices import TIPO_PRECIO_CHOICES
from .models import Categoria, Item, Banner, Cliente, Precio, Paquete, ImagenProducto
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

import locale

locale.setlocale(locale.LC_MONETARY, 'es_MX.UTF-8')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'estado')
    search_fields = ('nombre',)
    list_filter = ('estado',)
    ordering = ['nombre']

    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion')
        }),
        (_('Estado'), {
            'fields': ('estado',),
        })
    )

    related_modal_active = True

@admin.register(Categoria)
class CategoriaAdminAdmin(CategoriaAdmin):
    pass

class PrecioInline(admin.TabularInline):
    model = Precio
    extra = 0  # No agregar filas extras automáticamente
    fields = ('tipo_precio', 'precio', 'fecha_inicio', 'fecha_fin', 'activo',)
    can_delete = False  # No permitir eliminar precios predeterminados

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)

        # Cuando no hay precios asociados al producto, crear los precios por defecto
        if obj and not obj.precios.exists():
            for tipo, _ in TIPO_PRECIO_CHOICES:
                Precio.objects.create(
                    producto=obj,
                    tipo_precio=tipo[0],  # Accede al valor de la tupla
                    precio=0,  # Define un precio predeterminado
                    activo=(tipo[0] == 'Estándar'),  # Solo el tipo 'Estándar' será activo por defecto
                )
        return formset


class ImagenProductoInline(ImageUploaderInline):
    model = ImagenProducto
    fields = ['imagen']

    class Media:
        css = {
            'all': ('administrador/css/custom_admin.css',)
        }

# Definir el modelo de Producto
class ItemAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'mostrar_imagen', 'nombre', 'categoria', 'disponible', 'estado', 'creado_en', 'actualizado_en')
    search_fields = ('codigo', 'nombre', 'descripcion')
    list_filter = ('categoria', 'estado', 'disponible')
    ordering = ['nombre']

    fieldsets = (
        ('Información General', {
            'fields': (
                ('imagen_portada', ),
                ('tipo',),
                ('codigo', 'nombre'),
                ('descripcion',),
                ('categoria',),
                ('disponible', ),
                ('creado_en', 'actualizado_en')
            ),
            'classes': ('tab',),
        }),
    )

    readonly_fields = ('creado_en', 'actualizado_en')
    inlines = [ImagenProductoInline, PrecioInline]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'imagen_portada':
            kwargs['widget'] = ImageUploaderWidget()
        return super().formfield_for_dbfield(db_field, **kwargs)

    def mostrar_imagen(self, obj):
        if obj.imagen_portada:
            return mark_safe(f'<img src="{obj.imagen_portada.url}" style="max-width: 100px; height: auto;" />')
        return "-"

    mostrar_imagen.short_description = 'Imagen'


    class Media:
        css = {
            'all': ('administrador/css/custom_admin.css',)  # Asegúrate de que la ruta sea correcta
        }


@admin.register(Item)
class ItemAdminAdmin(ItemAdmin):
    pass


class PaqueteItemInline(admin.TabularInline):
    model = Paquete.productos.through  # Relación Many-to-Many entre Paquete e Item
    extra = 1  # Número de filas vacías que se mostrarán para agregar productos
    fields = ('item', 'imagen', 'precio')  # Nuevas columnas para imagen y precio
    readonly_fields = ('imagen', 'precio')  # Hacer que estas columnas sean solo lectura

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        return formset

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # No usar select_related para obtener campos no relacionados
        return queryset.select_related('item')  # Obtener el 'item' relacionado

    def imagen(self, obj):
        # Obtener la imagen del item relacionado
        if obj.item and obj.item.imagen_portada:
            return mark_safe(f'<img src="{obj.item.imagen_portada.url}" style="max-width: 100px; height: auto;" />')
        return "-"

    def precio(self, obj):
        # Obtener el precio del tipo "Estándar"
        precio = obj.item.precios.filter(tipo_precio='estandar').first()
        if precio:
            return f"${precio.precio:,.2f}"  # Formatear como precio con comas y decimales
        return "-"

    imagen.short_description = 'Imagen'
    precio.short_description = 'Precio Estándar'

    class Media:
        js = ('administrador/js/actualizar_item_inline.js',)


class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'mostrar_banner', 'descripcion', 'precio_formateado', 'fecha_inicio', 'fecha_fin', 'activo', )
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo',)
    ordering = ['nombre']

    fieldsets = (
        (None, {
            'fields': (
                ('banner', ),
                ('nombre',),
                ( 'descripcion',),
                ( 'precio',),
                ('fecha_inicio', 'fecha_fin',),
                ( 'activo', )
            )
        }),
    )

    inlines = [PaqueteItemInline]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'banner':
            kwargs['widget'] = ImageUploaderWidget()
        return super().formfield_for_dbfield(db_field, **kwargs)

    def mostrar_banner(self, obj):
        if obj.banner:
            return mark_safe(f'<img src="{obj.banner.url}" style="max-width: 100px; height: auto;" />')
        return "-"

    mostrar_banner.short_description = 'Banner'

    class Media:
        css = {
            'all': ('administrador/css/custom_admin.css',)  # Asegúrate de que la ruta sea correcta
        }

    def precio_formateado(self, obj):
        # Usamos el método number_format para formatear el número
        if obj.precio:
            return f"${obj.precio:,.2f}"  # Formato para moneda: ejemplo $1,000.00
        return "-"

    precio_formateado.short_description = 'Precio'

@admin.register(Paquete)
class PaqueteAdminAdmin(PaqueteAdmin):
    pass



# Definir el modelo de Banner
# NO SE ESTA USANDO POR EL MOMENTO
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo', 'creado_en', 'actualizado_en')
    search_fields = ('titulo',)
    list_filter = ('activo',)
    ordering = ['titulo']

    fieldsets = (
        (None, {
            'fields': ('titulo', 'imagen', 'url')
        }),
        (_('Estado'), {
            'fields': ('activo',),
        }),
        (_('Fechas'), {
            'fields': ('creado_en', 'actualizado_en'),
        }),
    )

    readonly_fields = ('creado_en', 'actualizado_en')


'''@admin.register(Banner)
class BannerAdminAdmin(BannerAdmin):
    pass'''


# Definir el modelo de Cliente
# NO SE ESTA USANDO POR EL MOMENTO
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'estado', 'registrado_en')
    search_fields = ('nombre', 'correo')
    list_filter = ('estado',)
    ordering = ['nombre']

    fieldsets = (
        (None, {
            'fields': ('nombre', 'correo', 'telefono', 'direccion')
        }),
        (_('Estado y Fechas'), {
            'fields': ('estado', 'registrado_en'),
        }),
    )

    readonly_fields = ('registrado_en',)


'''@admin.register(Cliente)
class ClienteAdminAdmin(ClienteAdmin):
    pass'''
