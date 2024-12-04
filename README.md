# Proyecto: Página Web Dinámica - REX DEVELOP

## Descripción

Este proyecto corresponde al desarrollo de una página web dinámica para gestionar productos y servicios. El sitio cuenta con un panel de administración donde los clientes pueden gestionar su catálogo de productos y servicios de manera fácil y eficiente.

### Funcionalidades principales

- **Gestión de Productos y Servicios**: Agregar, editar y eliminar productos y servicios a través de un panel de administración intuitivo.
- **Precios Variables**: Definir múltiples tipos de precios para cada producto o servicio (Precio Estándar, Precio Mayoreo, Precio Oferta, Precio Distribuidor).
- **Categorías de Productos**: Organizar los productos en categorías (Ejemplo: Electrónica, Moda, Hogar).
- **Panel de Administración**: Gestión de productos y servicios sin necesidad de intervención técnica.

---

## Requisitos

- **Python 3.x**
- **Django 5.x**
- **MySQL** (u otra base de datos compatible)

---

## Instalación

1. **Clonar el repositorio**

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Instalar dependencias**

    Asegúrate de tener un entorno virtual configurado. Si no tienes `virtualenv` instalado, puedes instalarlo con:

    ```bash
    pip install virtualenv
    ```

    Luego, crea el entorno virtual y activa el entorno:

    ```bash
    virtualenv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

    Después, instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar base de datos**

    Si estás utilizando **PostgreSQL**, asegúrate de que las credenciales de la base de datos estén configuradas correctamente en el archivo `settings.py` de Django. Modifica la configuración de la base de datos a:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_base_de_datos',
            'USER': 'nombre_usuario',
            'PASSWORD': 'contraseña',
            'HOST': 'localhost',  # O la IP de tu servidor de base de datos
            'PORT': '5432',  # Puerto de PostgreSQL
        }
    }
    ```

4. **Migraciones**

    Ejecuta las migraciones para crear las tablas en la base de datos:

    ```bash
    python manage.py migrate
    ```

5. **Cargar datos iniciales (Opcional)**

    Si deseas cargar categorías y productos de forma masiva, asegúrate de tener los archivos `Excel` listos y sigue el proceso de carga inicial que se describe más abajo.

6. **Iniciar el servidor de desarrollo**

    ```bash
    python manage.py runserver
    ```

    Accede a la aplicación en [http://localhost:8000](http://localhost:8000).
## Proceso de Carga Inicial de Productos y Servicios

### Para facilitar la carga de productos y servicios, completa el archivo **Excel** con los siguientes datos:

#### Hoja 1: Productos

| Código Producto | Tipo     | Categoría   | Nombre Producto | Descripción                | Precio Estándar | Precio Mayoreo | Precio Oferta | Precio Distribuidor | Imagen Portada | Imagen Producto 1 | Imagen Producto 2 | Imagen Producto 3 |
| --------------- | -------- | ----------- | --------------- | -------------------------- | --------------- | -------------- | ------------- | ------------------- | -------------- | ----------------- | ----------------- | ----------------- |
| PROD-001        | Producto | Electrónica | Producto 1      | Descripción del Producto 1 | 100.00          | 90.00          | 80.00         | 70.00               | portada_1.jpg  | producto_1_1.jpg  | producto_1_2.jpg  | producto_1_3.jpg  |
| PROD-002        | Producto | Hogar       | Producto 2      | Descripción del Producto 2 | 200.00          | 180.00         | 160.00        | 140.00              | portada_2.jpg  | producto_2_1.jpg  | producto_2_2.jpg  | -                 |
| PROD-003        | Producto | Moda        | Producto 3      | Descripción del Producto 3 | 300.00          | -              | -             | -                   | portada_3.jpg  | producto_3_1.jpg  | -                 | -                 |
| PROD-004        | Producto | Oficina     | Producto 4      | Descripción del Producto 4 | -               | -              | -             | -                   | -              | -                 | -                 | -                 |

**Campos Obligatorios**:

- **Código Producto**: Código único para identificar el producto o servicio.
- **Tipo**: Tipo de item (Producto o Servicio).
- **Categoría**: La categoría del producto o servicio.
- **Nombre Producto**: El nombre del producto o servicio.
- **Descripción**: Descripción detallada del producto o servicio.
- **Precio Estándar**: El precio regular del producto o servicio.
- **Imagen Portada**: Nombre del archivo de la imagen principal del producto o servicio (puede dejarse vacío si no aplica).

**Campos Opcionales**:

- **Precio Mayoreo**: El precio para el tipo de precio "Mayoreo" (puede dejarse vacío).
- **Precio Oferta**: El precio para el tipo de precio "Oferta" (puede dejarse vacío).
- **Precio Distribuidor**: El precio para el tipo de precio "Distribuidor" (puede dejarse vacío).
- **Imagen Producto 1, 2, 3**: Nombre de archivos para imágenes adicionales del producto (opcional). Puede dejar los campos vacíos si no aplica.

**Ejemplo de carga de un producto sin imagen de portada, precios, ni imágenes adicionales**:

| Código Producto | Tipo     | Categoría   | Nombre Producto | Descripción                | Precio Estándar | Precio Mayoreo | Precio Oferta | Precio Distribuidor | Imagen Portada | Imagen Producto 1 | Imagen Producto 2 | Imagen Producto 3 |
| --------------- | -------- | ----------- | --------------- | -------------------------- | --------------- | -------------- | ------------- | ------------------- | -------------- | ----------------- | ----------------- | ----------------- |
| PROD-004        | Producto | Oficina     | Producto 4      | Descripción del Producto 4 | -               | -              | -             | -                   | -              | -                 | -                 | -                 |

Este ejemplo muestra cómo se puede cargar un producto sin precio, imagen de portada o imágenes adicionales, permitiendo flexibilidad para productos sin esta información.

---


### Imágenes

- **Formato de imágenes**: Las imágenes deben estar en formato **JPG**, **PNG**, o **GIF**.
- **Resolución recomendada**:
    - **Productos**: Al menos **800x800 píxeles** para la imagen de portada.
    - **Imágenes adicionales**: Mínimo **400x400 píxeles**.
- **Carpeta de imágenes**: Organiza las imágenes en un archivo comprimido (**.zip**) en la **raíz** del proyecto, asegurándote de que no haya subcarpetas. Los **nombres de archivos** de las imágenes deben coincidir con los especificados en el archivo Excel (por ejemplo, `portada_1.jpg`, `producto_1_1.jpg`).

**Importante**: Asegúrate de que todas las imágenes estén en el mismo nivel dentro del archivo ZIP, sin subcarpetas.


***REXDEVELOP***