from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_ui():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/") 

    try:
        # Esperar hasta que el enlace "Crear Noticia" esté presente y haz clic en él
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Crear Noticia"))
        ).click()

        # Esperar hasta que el formulario esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "noticia-form"))
        )

        # Llenar el formulario
        driver.find_element(By.ID, "titulo").send_keys("Título de prueba")
        driver.find_element(By.ID, "cuerpo").send_keys("Cuerpo de prueba")
        driver.find_element(By.ID, "archivo").send_keys("C:/ruta/a/tu/imagen.jpg")  # Asegúrate de que la imagen existe
        driver.find_element(By.ID, "fecha").send_keys("2023-05-27")

        # Enviar el formulario
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Esperar hasta que la redirección o la confirmación aparezca
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # Verificar que estamos en la página de confirmación o lista de noticias
        assert "Noticia" in driver.page_source  # Esto debe cambiarse dependiendo de tu implementación específica

        print("Test passed!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui()
