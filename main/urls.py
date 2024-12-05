# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('static/mexbull/', views.index, name='index'),  # Ruta para la página de inicio
    path('static/mexbull/', views.about, name='about'),  # Ruta para la página "about"
    path('obtener_imagen_y_precio/<int:item_id>/', views.obtener_imagen_y_precio, name='obtener_imagen_y_precio'),
]

