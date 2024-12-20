from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Ruta para la página de inicio
    path('about/', views.AboutView.as_view(), name='about'),  # Ruta para la página "about"
    path('contact/', views.ContactView.as_view(), name='contact'),  # Ruta para la página "contact"

    # Front de articulos
    path('productos/', views.ProductosView.as_view(), name='productos'),  # Ruta para la página "productos"
    path('producto/<int:producto_id>', views.ProductoView.as_view(), name='producto'),

    path('paquetes/', views.PaquetesView.as_view(), name='paquetes'),  # Ruta para la página "paquetes"
    path('paquete/<int:paquete_id>/', views.PaquetePostView.as_view(), name='paquete'),

    path('servicios/', views.MenuMediumView.as_view(), name='servicios'),  # Ruta para la página "servicios"

    path('shopping-cart/', views.ShoppingCartView.as_view(), name='shopping-cart'),
    # Ruta para la página "shopping-cart"
    path('shopping-checkout/', views.ShoppingCheckoutView.as_view(), name='shopping-checkout'),
    # Ruta para la página "shopping-checkout"
    path('single-post/', views.PaquetePostView.as_view(), name='single-post'),  # Ruta para la página "single-post"

    path('blog/', views.BlogView.as_view(), name='blog'),  # Ruta para la página "single-post"
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),  # Ruta para la página "delivery"
    path('error-404/', views.Error404View.as_view(), name='error-404'),  # Ruta para la página "error-404"
    path('under-construction/', views.UnderConstructionView.as_view(), name='under-Construction'),
    # Ruta para la página "under-construcction"

    # Ruta para imagen y precio en los inlines para paquetes en el Administrador
    path('obtener_imagen_y_precio/<int:item_id>/', views.ObtenerImagenYPrecioView.as_view(),
         name='obtener_imagen_y_precio'),
]
