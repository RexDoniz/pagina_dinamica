from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item, Precio
from .choices import TIPO_PRECIO_CHOICES  # Asegúrate de tener este import

@receiver(post_save, sender=Item)
def crear_precios_predeterminados(sender, instance, created, **kwargs):
    if created:
        for tipo, _ in TIPO_PRECIO_CHOICES:
            # Crear precios predeterminados, el primero (estandar) será activo
            Precio.objects.create(
                producto=instance,
                tipo_precio=tipo,
                precio=0,
                activo=(tipo == 'estandar'),  # Solo el tipo 'estandar' estará activo por defecto
            )
