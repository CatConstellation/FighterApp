document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const noticiaId = params.get('id');

    if (noticiaId) {
        fetch(`/api/v1/noticias/${noticiaId}`)
            .then(response => response.json())
            .then(noticia => {
                document.getElementById('titulo').innerText = noticia.titulo;
                document.getElementById('imagen').src = noticia.archivo;
                document.getElementById('contenido').innerText = noticia.cuerpo;
                document.getElementById('fecha').innerText = `Fecha: ${noticia.fecha}`;
            })
            .catch(error => {
                console.error('Error cargando la noticia:', error);
                alert('No se pudo cargar la noticia. Intenta de nuevo más tarde.');
            });
    } else {
        alert('No se proporcionó un ID de noticia válido.');
    }
});
