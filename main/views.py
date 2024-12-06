# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

from .models import Item


def obtener_imagen_y_precio(request, item_id):
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



def index(request):
    return render(request, 'index.html')  # Cargar el archivo index.html

def about(request):
    return render(request, 'about.html')  # Cargar el archivo about.html


def contact(request):
    return render(request, 'contact.html')  # Cargar el archivo contact.html


def menu(request):
    return render(request, 'menu.html')  # Cargar el archivo menu.html

def menuBig(request):
    return render(request, 'menu-big.html')  # Cargar el archivo menu-big.html

def menuMedium(request):
    return render(request, 'menu-medium.html')  # Cargar el archivo menu-medium.html


def shoppingCart(request):
    return render(request, 'shopping-cart.html')  # Cargar el archivo shopping-cart.html


def shoppingCheckout(request):
    return render(request, 'shopping-checkout.html')  # Cargar el archivo shopping-checkout.html


def singlePost(request):
    return render(request, 'single-post.html')  # Cargar el archivo single-post.html

def blog(request):
    return render(request, 'blog.html')  # Cargar el archivo blog.html

def delivery(request):
    return render(request, 'delivery.html')  # Cargar el archivo delivery.html

def error404(request):
    return render(request, 'error-404.html')  # Cargar el archivo error-404.html