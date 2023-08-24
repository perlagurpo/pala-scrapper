from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador (asegúrate de tener el controlador adecuado para tu navegador)
# Descarga el controlador de Chrome en: https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome(executable_path="ruta_al_controlador_de_chrome")

# Abrir el sitio web de Google
driver.get("https://www.google.com")

# Encontrar el campo de búsqueda y escribir la palabra deseada
search_box = driver.find_element_by_name("q")
search_term = input("Ingrese la palabra de búsqueda: ")
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

# Esperar un momento para que se carguen los resultados (puede ser ajustado según tu conexión)
time.sleep(2)

# Encontrar los enlaces de los resultados de búsqueda
search_results = driver.find_elements_by_xpath("//div[@class='tF2Cxc']/div[@class='yuRUbf']/a")

# Guardar los enlaces de los primeros 10 resultados
result_links = [result.get_attribute("href") for result in search_results[:10]]

# Imprimir los enlaces
for i, link in enumerate(result_links):
    print(f"Resultado {i + 1}: {link}")

# Cerrar el navegador
driver.quit()
