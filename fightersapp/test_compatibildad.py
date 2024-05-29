from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_compatibilidad():
    # Probar en diferentes navegadores
    for browser in ["Chrome", "Firefox", "Edge"]:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Edge":
            driver = webdriver.Edge()

        try:
            driver.get("http://127.0.0.1:8000/")
            
            # Esperar a que el enlace "Crear Noticia" esté presente y hacer clic en él
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Crear Noticia"))
            ).click()

            # Esperar a que el formulario esté presente
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "noticia-form"))
            )

            # Verificar que el campo "titulo" esté presente
            assert driver.find_element(By.ID, "titulo").is_displayed()
            print(f"Test passed on {browser}!")

        except Exception as e:
            print(f"An error occurred on {browser}: {e}")
        
        finally:
            driver.quit()

if __name__ == "__main__":
    test_compatibilidad()
