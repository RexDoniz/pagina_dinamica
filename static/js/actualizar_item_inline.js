document.addEventListener('DOMContentLoaded', function () {
    // Escuchar cambios en el campo 'item' dentro de cada fila del inline
    document.querySelectorAll('.field-item select').forEach(function(select) {
        // Escuchar el evento change del Select2
        $(select).on('change', function() {
            var row = select.closest('tr');  // Encontrar la fila actual

            var itemId = select.value;  // Obtener el ID del item seleccionado

            if (itemId) {
                // Realizar una solicitud AJAX para obtener la imagen y el precio del Item
                fetch(`/main/obtener_imagen_y_precio/${itemId}/`)
                    .then(response => response.json())
                    .then(data => {
                        var imagenUrl = data.imagen;
                        var precio = data.precio;

                        // Actualizar las columnas de la imagen y precio
                        if (imagenUrl) {
                            row.querySelector('.field-imagen p').innerHTML = `<img src="${imagenUrl}" style="max-width: 100px; height: auto;" />`;
                        }
                        if (precio) {
                            row.querySelector('.field-precio p').innerText = `$${precio}`;
                        }
                    })
                    .catch(error => console.error('Error al obtener la imagen y el precio:', error));
            }
        });
    });
});
