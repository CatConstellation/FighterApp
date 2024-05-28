document.addEventListener('DOMContentLoaded', () => {
    const archivoInput = document.getElementById('archivo');
    archivoInput.addEventListener('change', () => {
        const file = archivoInput.files[0];
        const preview = document.getElementById('image-preview');
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                preview.src = e.target.result;
                preview.classList.remove('hidden');
            };
            reader.readAsDataURL(file);
        } else {
            preview.classList.add('hidden');
        }
    });
});

function redirectToNoticiasPage() {
    window.location.href = "/";
}
