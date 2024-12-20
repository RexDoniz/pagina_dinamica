from main.choices import TIPO_CHOICES

def tipos(request):
    # Obtener solo los valores de tipo
    tipos = [tipo[0] for tipo in TIPO_CHOICES]  # Extrae solo el valor, que es el nombre del tipo
    return {'tipos': tipos}
