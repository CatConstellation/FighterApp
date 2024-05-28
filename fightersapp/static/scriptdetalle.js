document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const noticiaId = params.get('id');

    fetch(`/api/v1/noticias/${noticiaId}`)
        .then(response => response.json())
        .then(noticia => {
            document.getElementById('titulo').innerText = noticia.titulo;
            document.getElementById('imagen').src = noticia.imagenUrl;
            document.getElementById('contenido').innerText = noticia.cuerpo;
            document.getElementById('fecha').innerText = `Fecha: ${noticia.fecha}`;
        });
});
