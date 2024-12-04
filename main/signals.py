from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from .models import Item, Precio
from .choices import TIPO_PRECIO_CHOICES  # Asegúrate de tener este import

@receiver(post_save, sender=Item)
def crear_precios_predeterminados(sender, instance, created, **kwargs):
    if created:
        for tipo, descripcion in TIPO_PRECIO_CHOICES:
            Precio.objects.create(
                producto=instance,
                tipo_precio=tipo,
                precio=0,
                fecha_inicio=now(),
                activo=(tipo == 'estandar'),
            )
