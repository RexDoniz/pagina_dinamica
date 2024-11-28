from django.contrib import admin

from .choices import TIPO_PRECIO_CHOICES
from .models import Categoria, Item, Banner, Cliente, Precio, Paquete
from django.utils.translation import gettext_lazy as _


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'estado')  # Asegúrate de que los campos sean accesibles
    search_fields = ('nombre',)
    list_filter = ('estado',)  # Asegúrate de que 'estado' sea un campo en el modelo
    ordering = ['nombre']

    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion')
        }),
        (_('Estado'), {
            'fields': ('estado',),
        })
    )

@admin.register(Categoria)
class CategoriaAdminAdmin(CategoriaAdmin):
    pass

class PrecioInline(admin.TabularInline):
    model = Precio
    extra = 0  # No agregar filas extras automáticamente
    fields = ('tipo_precio', 'precio', 'descripcion', 'activo',)
    readonly_fields = ('tipo_precio',)
    can_delete = False  # No permitir eliminar precios predeterminados

    def has_add_permission(self, request, obj):
        return False  # No permitir agregar nuevos precios desde el inline

    def get_formset(self, request, obj=None, **kwargs):
        """ Personaliza el formulario para el inline """
        formset = super().get_formset(request, obj, **kwargs)

        # Cuando no hay precios asociados al producto, crear los precios por defecto.
        if obj and not obj.precios.exists():
            for tipo, _ in TIPO_PRECIO_CHOICES:
                Precio.objects.create(
                    producto=obj,
                    tipo_precio=tipo,
                    activo=(tipo == 'estandar'),  # Solo el tipo 'estandar' será activo por defecto
                )
        return formset


# Definir el modelo de Producto
class ItemAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'disponible', 'estado', 'creado_en', 'actualizado_en')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria', 'estado', 'disponible')
    ordering = ['nombre']

    # Definir los inlines para incluir el paquete de productos (si aplica en tu caso)
    fieldsets = (
        (None, {
            'fields': (
                ('codigo', ),
                ('tipo',),
                ('nombre', ),
                ('descripcion',),
                ('categoria',),
                ('imagen', ),
                ('disponible', )
            )
        }),
        (_('Fechas'), {
            'fields': ('creado_en', 'actualizado_en'),
        }),
    )

    readonly_fields = ('creado_en', 'actualizado_en')
    inlines = [PrecioInline]


@admin.register(Item)
class ItemAdminAdmin(ItemAdmin):
    pass

# Inline para agregar Items al Paquete
class PaqueteItemInline(admin.TabularInline):
    model = Paquete.productos.through  # Relación Many-to-Many entre Paquete e Item
    extra = 1  # Número de filas vacías que se mostrarán para agregar productos
    fields = ('item',)  # Solo mostrar el campo 'item' que es el modelo relacionado

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        return formset

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Usar select_related para mejorar la eficiencia de la consulta de datos relacionados
        return queryset.select_related('item__categoria')


class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'fecha_inicio', 'fecha_fin', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo',)
    ordering = ['nombre']

    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'precio', 'fecha_inicio', 'fecha_fin', 'activo')
        }),
    )

    inlines = [PaqueteItemInline]  # Añadir el inline para agregar productos al paquete

@admin.register(Paquete)
class PaqueteAdminAdmin(PaqueteAdmin):
    pass



# Definir el modelo de Banner
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


@admin.register(Banner)
class BannerAdminAdmin(BannerAdmin):
    pass


# Definir el modelo de Cliente
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


@admin.register(Cliente)
class ClienteAdminAdmin(ClienteAdmin):
    pass
