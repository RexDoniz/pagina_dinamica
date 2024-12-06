# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('about/', views.about, name='about'),  # Ruta para la página "about"
    path('contact/', views.contact, name='contact'),  # Ruta para la página "contact"
    path('menu/', views.menu, name='menu'),  # Ruta para la página "menu"
    path('menu-big/', views.menuBig, name='menu-big'),  # Ruta para la página "menu-big"
    path('menu-medium/', views.menuMedium, name='menu-medium'),  # Ruta para la página "menu-medium"
    path('shopping-cart/', views.shoppingCart, name='shopping-cart'),  # Ruta para la página "shopping-cart"
    path('shopping-checkout/', views.shoppingCheckout, name='shopping-checkout'),  # Ruta para la página "shopping-checkout"
    path('single-post/', views.singlePost, name='single-post'),  # Ruta para la página "single-post"

    path('blog/', views.blog, name='blog'),  # Ruta para la página "single-post"
    path('delivery/', views.delivery, name='delivery'),  # Ruta para la página "delivery"
    path('error-404/', views.error404, name='error-404'),  # Ruta para la página "error-404"

    # Ruta para imagen y precio en los inlines para paquetes en el Administrador
    path('obtener_imagen_y_precio/<int:item_id>/', views.obtener_imagen_y_precio, name='obtener_imagen_y_precio'),
]

