const imagenInput = document.getElementById("imagenInput");
const publicarButton = document.getElementById("publicarButton");

publicarButton.addEventListener("click", () => {
  const imagenUrl = imagenInput.value;
  if (imagenUrl) {
    const noticia = document.createElement("div");
    noticia.classList.add("noticia");

    const titulo = document.createElement("h2");
    titulo.textContent = "Encabezado de la noticia";
    noticia.appendChild(titulo);

    const imagen = document.createElement("img");
    imagen.src = imagenUrl;
    noticia.appendChild(imagen);

    const contenido = document.createElement("p");
    contenido.textContent = "Contenido de la noticia";
    noticia.appendChild(contenido);

    document.getElementById("noticias").appendChild(noticia);
  } else {
    alert("Debes agregar una imagen para publicar la noticia");
  }
});