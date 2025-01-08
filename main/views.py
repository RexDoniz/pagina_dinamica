from django.http import JsonResponse
import random

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Paquete, Item, Categoria

# Vista para obtener imagen y precio del item en formato JSON
class ObtenerImagenYPrecioView(TemplateView):
    def get(self, request, item_id, *args, **kwargs):
        try:
            item = Item.objects.get(id=item_id)
            imagen_url = item.imagen_portada.url if item.imagen_portada else ""
            precio_estandar = item.precios.filter(tipo_precio="estandar").first()
            precio = precio_estandar.precio if precio_estandar else "0.00"

            return JsonResponse({
                'imagen': imagen_url,
                'precio': precio
            })
        except Item.DoesNotExist:
            return JsonResponse({'error': 'Item no encontrado'}, status=404)


# Vista para la página de inicio (index)
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtén los paquetes activos
        paquetes = Paquete.objects.filter(activo=True)
        # Obtén los items disponibles y activos
        items = Item.objects.filter(disponible=True, estado=True)

        # Selecciona un item aleatorio
        item_seleccionado = random.choice(items) if items else None

        if item_seleccionado:
            item_seleccionado.precio_estandar = item_seleccionado.precios.filter(tipo_precio='estandar',
                                                                                 activo=True).first()
        else:
            item_seleccionado = None

        # Transiciones de animación
        transitions = [
            'slideoverup', 'slideoverdown', 'slideoverright', 'slideoverleft', 'slideoverhorizontal', 'slideoververtical'
        ]
        for paquete in paquetes:
            paquete.transition = random.choice(transitions)

        # Añadir los paquetes y el item seleccionado al contexto
        context['paquetes'] = paquetes
        context['item'] = item_seleccionado
        return context


# Vista para la página "About"
class AboutView(TemplateView):
    template_name = 'about.html'


# Vista para la página de contacto
class ContactView(TemplateView):
    template_name = 'contact.html'


# Vista para la página "Productos"
class ProductosView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener todas las categorías activas
        categorias = Categoria.objects.filter(estado=True)

        # Agrupar productos por categoría
        categorias_con_productos = []
        for categoria in categorias:
            productos = Item.objects.filter(categoria=categoria, disponible=True, estado=True, tipo="productos")

            # Obtener el precio estándar de cada producto
            for producto in productos:
                precio_estandar = producto.precios.filter(tipo_precio="estandar", activo=True).first()
                # Pasar el precio estándar al producto
                producto.precio_estandar = precio_estandar.precio if precio_estandar else None

            categorias_con_productos.append({
                'categoria': categoria,
                'productos': productos
            })

        # Pasar la lista de categorías con sus productos al contexto
        context['categorias_con_productos'] = categorias_con_productos

        return context


# Vista para la página "Producto"
class ProductoView(TemplateView):
    template_name = 'single-item.html'

    def dispatch(self, request, *args, **kwargs):
        """Maneja la solicitud y redirige si el producto no es válido."""
        self.producto_id = self.kwargs.get('producto_id')
        if not self.producto_id:
            return redirect('index')
        self.item = self.obtener_item(self.producto_id)
        if not self.item:
            return redirect('index')  # Redirigir si el producto no fue encontrado
        return super().dispatch(request, *args, **kwargs)

    def obtener_item(self, producto_id):
        """Encapsula la lógica de obtención del producto con manejo de excepciones."""
        try:
            return Item.objects.filter(
                id=producto_id,
                disponible=True,
                estado=True
            ).first()
        except Exception as e:
            # Esto podría registrarse en un log
            return None

    def get_context_data(self, **kwargs):
        """Añade `self.item` al contexto de la vista."""
        context = super().get_context_data(**kwargs)
        context['item'] = self.item
        return context



class PaquetesView(TemplateView):
    template_name = 'menu-big.html'

    def get_context_data(self, **kwargs):
        # Obtener el contexto base
        context = super().get_context_data(**kwargs)

        # Verificar si existe un paquete_id en los parámetros de la URL
        paquete_id = self.kwargs.get('paquete_id')

        if paquete_id:
            # Si se pasa el ID, obtener solo el paquete correspondiente
            paquete = get_object_or_404(Paquete, id=paquete_id, activo=True)
            context['paquete'] = paquete  # Pasar el paquete al contexto
            # Obtener los productos con sus precios estandar
            productos = []
            for producto in paquete.productos.all():
                precio_estandar = producto.precios.filter(tipo_precio='estandar').first()
                productos.append({
                    'producto': producto,
                    'precio_estandar': precio_estandar.precio if precio_estandar else None
                })
            context['productos'] = productos  # Pasar los productos con precio estándar al contexto
        else:
            # Si no se pasa el ID, mostrar todos los paquetes
            context['paquetes'] = Paquete.objects.filter(activo=True)  # Agregar todos los paquetes activos

        return context

# Vista para la página "Menu Big"
class PaquetePostView(TemplateView):
    template_name = 'single-post.html'

    def dispatch(self, request, *args, **kwargs):
        # Verificar si existe un paquete_id en los parámetros de la URL
        paquete_id = self.kwargs.get('paquete_id')

        if paquete_id:
            # Si el paquete no existe, redirigir al inicio
            paquete = Paquete.objects.filter(id=paquete_id, activo=True).first()
            if not paquete:
                return redirect(reverse('index'))  # Redirigir si no existe el paquete
        else:
            return redirect(reverse('index'))  # Redirigir si no se pasa el ID

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paquete_id = self.kwargs.get('paquete_id')

        if paquete_id:
            paquete = Paquete.objects.get(id=paquete_id)
            context['paquete'] = paquete  # Agregar el paquete al contexto
        return context

# Vista para la página "Menu Medium"
class MenuMediumView(TemplateView):
    template_name = 'menu-medium.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtrar solo los items cuyo tipo es 'servicio'
        servicios = Item.objects.filter(tipo='servicios', disponible=True, estado=True)
        # Agrupar los servicios según su categoría
        categorias = Categoria.objects.filter(estado=True)
        categorias_con_servicios = []
        for categoria in categorias:
            servicios_en_categoria = servicios.filter(categoria=categoria)

            for servicio in servicios_en_categoria:
                precio_estandar = servicio.precios.filter(tipo_precio="estandar", activo=True).first()
                # Pasar el precio estándar al producto
                servicio.precio_estandar = precio_estandar.precio if precio_estandar else None

            if servicios_en_categoria.exists():  # Solo incluir categorías con servicios
                categorias_con_servicios.append({
                    'categoria': categoria,
                    'servicios': servicios_en_categoria
                })
        # Agregar las categorías con servicios a la plantilla
        context['categorias_con_servicios'] = categorias_con_servicios
        return context


# Vista para la página de "Shopping Cart"
class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'


# Vista para la página de "Shopping Checkout"
class ShoppingCheckoutView(TemplateView):
    template_name = 'shopping-checkout.html'


# Vista para la página de Blog
class BlogView(TemplateView):
    template_name = 'blog.html'


# Vista para la página de Delivery
class DeliveryView(TemplateView):
    template_name = 'delivery.html'


# Vista para la página 404
class Error404View(TemplateView):
    template_name = 'error-404.html'


# Vista para la página "Under Construction"
class UnderConstructionView(TemplateView):
    template_name = 'under-construction.html'
