JAZZMIN_SETTINGS = {
    "site_title": "Administrador",
    "site_header": "Página Dinámica",
    "site_brand": "Página Dinámica",
    # "site_logo": "img/logo.png",  # Logo del sitio
    "welcome_sign": "Bienvenido al Administrador",
    "user_themes": True,

    "search_model": [
        "main.Item",
    ],

    "copyright": "REX DEVELOP",
    "site_logo_classes": "rounded-circle",
    "custom_css": "css/custom_admin.css",  # Archivo CSS personalizado para el administrador

    "topmenu_links": [
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "main"},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "related_modal_active": True,
    "show_ui_builder": False,
    "changeform_format": "single",  # Formato del formulario (único)

    "custom_links": {
        "main": [{
            "name": "Documentación",
            "url": "hhttps://www.google.com.mx/",
            "icon": "fas fa-bookmark",
            "permissions": ["main.view_producto"]
        }],
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main": "fas fa-home",
        "main.Categoria": "fas fa-th-large",
        "main.Item": "fas fa-list",
        "main.Precio": "fas fa-dollar-sign",
        #"main.Banner": "fas fa-images",
        # "main.Cliente": "fas fa-users",
        "main.Paquete": "fas fa-box",
    },

    # Excluir modelos específicos de la vista de administración
    "hide_models": [
        "auth.Group",
        "main.Banner",
        "main.Cliente"
    ]
}


JAZZMIN_UI_TWEAKS = {
    "theme": "litera",  # Tema predeterminado
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "#44475a",
    "accent": "accent-olive",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-pink",
    "sidebar_nav_small_text": "sidebar-dark-pink",
    "sidebar_nav_child_indent": False,
    "navbar_fixed": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "navbar_header_background": "#44475a",  # Fondo de la cabecera
    "navbar_header_color": "#f8f8f2",  # Color del texto en la cabecera
    "primary_button_bg": "#ff79c6",  # Fondo del botón principal
    "secondary_button_bg": "#8be9fd",  # Fondo del botón secundario
    "link_color": "#8be9fd",  # Color de los enlaces
    "link_hover_color": "#bd93f9",  # Color de los enlaces al pasar el ratón
    "sidebar_nav_link_color": "#f8f8f2",  # Color de los enlaces en la barra lateral
    "sidebar_nav_active_background": "#44475a",  # Fondo del enlace activo
    "actions_sticky_top": False,
}
