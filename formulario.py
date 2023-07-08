from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()

driver.get("C:\\Users\\PC\\Documents\\Otros\\Elias\\2023\\calidad software\\formulario.html")
nombre_input = driver.find_element(By.ID, "nombre")
nombre_input.clear()
nombre_input.send_keys("Elias")


apellido_input = driver.find_element(By.ID, "apellido")
apellido_input.clear()
apellido_input.send_keys("Llampi")

correo_input = driver.find_element(By.ID, "correo")
correo_input.clear()
correo_input.send_keys("correo@gmail.com")

time.sleep(3)

confirmar = driver.find_element(By.ID,"confirm")
confirmar.click()

time.sleep(2)

alert = Alert(driver)

print(alert.text)
print ("Se almacenaron los dato exitosamente")