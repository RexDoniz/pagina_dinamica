# main/apps.py
from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        # Importa y registra las señales
        import main.signals
