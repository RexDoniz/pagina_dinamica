# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('obtener_imagen_y_precio/<int:item_id>/', views.obtener_imagen_y_precio, name='obtener_imagen_y_precio'),
]

