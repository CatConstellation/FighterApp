const eliminarNoticiaForm = document.getElementById('eliminar-noticia-form');

eliminarNoticiaForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  const confirmDelete = confirm("¿Está seguro de eliminar esta noticia?");
  if (confirmDelete) {
    fetch(eliminarNoticiaForm.action, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the backend
      if (data.message === 'Noticia eliminada correctamente') {
        // Deletion successful
        alert('Noticia eliminada con éxito!');
        // (Optionally, redirect or update the page)
      } else {
        // Deletion failed
        alert('Error al eliminar la noticia: ' + data.detail);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error inesperado al eliminar la noticia. Por favor vuelva a intentar');
    });
  }
});
