from django.core.management.base import BaseCommand
from main.models import Categoria


class Command(BaseCommand):
    help = 'Poblar la tabla de categorías con valores por defecto'

    def handle(self, *args, **kwargs):
        categorias_default = [
            {'nombre': 'Electrónica', 'descripcion': 'Dispositivos electrónicos y gadgets'},
            {'nombre': 'Moda', 'descripcion': 'Ropa, calzado y accesorios'},
            {'nombre': 'Hogar', 'descripcion': 'Productos para el hogar y decoración'},
        ]

        for categoria in categorias_default:
            Categoria.objects.get_or_create(**categoria)

        self.stdout.write(self.style.SUCCESS('¡Categorías predeterminadas creadas correctamente!'))
