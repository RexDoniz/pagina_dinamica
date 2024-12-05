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
    return render(request, 'mexbull/index.html')  # Cargar el archivo index.html

def about(request):
    return render(request, 'mexbull/about.html')  # Cargar el archivo about.html