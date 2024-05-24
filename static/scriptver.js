document.addEventListener('DOMContentLoaded', () => {
    obtenerNoticias();

    const searchInput = document.getElementById('search');
    searchInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            buscarNoticias(searchInput.value);
        }
    });

    const searchButton = document.getElementById('search-button');
    searchButton.addEventListener('click', () => {
        buscarNoticias(searchInput.value);
    });

    const createButton = document.getElementById('create-button');
    createButton.addEventListener('click', () => {
        window.location.href = "/crearnoticia.html";
    });
});

async function obtenerNoticias() {
    try {
        const respuesta = await fetch('/api/v1/noticias/');
        const datos = await respuesta.json();

        if (respuesta.ok) {
            mostrarNoticias(datos);
        } else {
            console.error('Error al obtener las noticias:', datos);
        }
    } catch (error) {
        console.error('Error al obtener las noticias:', error);
    }
}

async function buscarNoticias(query) {
    try {
        const respuesta = await fetch(`/api/v1/noticias/buscar/?query=${encodeURIComponent(query)}`);
        const datos = await respuesta.json();

        if (respuesta.ok) {
            mostrarNoticias(datos);
        } else {
            console.error('Error al buscar noticias:', datos);
        }
    } catch (error) {
        console.error('Error al buscar noticias:', error);
    }
}

function mostrarNoticias(noticias) {
    const noticiasList = document.getElementById('noticias-list');
    noticiasList.innerHTML = '';

    noticias.forEach(noticia => {
        const noticiaHTML = `
            <article class="noticia">
                <img src="${noticia.archivo}" alt="${noticia.titulo}">
                <div class="noticia-info">
                    <h2>${noticia.titulo}</h2>
                    <p>${noticia.cuerpo}</p>
                </div>
                <div class="actions">
                    <button onclick="eliminarNoticia(${noticia.id_noticia})">
                        <img src="/static/images/trash-icon.png" alt="Eliminar">
                    </button>
                    <button>
                        <img src="/static/images/bell-icon.png" alt="Notificar">
                    </button>
                </div>
            </article>
        `;
        noticiasList.insertAdjacentHTML('beforeend', noticiaHTML);
    });
}

async function eliminarNoticia(id_noticia) {
    if (!confirm('¿Estás seguro de que deseas eliminar esta noticia?')) {
        return;
    }

    try {
        const respuesta = await fetch(`/api/v1/noticias/${id_noticia}`, {
            method: 'DELETE'
        });

        if (respuesta.ok) {
            alert('Noticia eliminada');
            obtenerNoticias();
        } else {
            const errorData = await respuesta.json();
            console.error('Error al eliminar la noticia:', errorData);
            alert('Error al eliminar la noticia');
        }
    } catch (error) {
        console.error('Error al eliminar la noticia:', error);
        alert('Error al eliminar la noticia');
    }
}
