from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.service import ChromiumService
import time



correios_link = "https://buscacepinter.correios.com.br/app/endereco/index.php"
driver = webdriver.Chrome()

driver.get(correios_link)

cep_input = driver.find_element(By.NAME, "endereco")
cep_input.send_keys("07858230")

find_button = driver.find_element(By.XPATH, "//button[text()='Buscar']")
find_button.click()

time.sleep(3)

table = driver.find_element(By.ID, "resultado-DNEC")
address = table.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
neighborhood = table.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
state =  table.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text

print("Endereço: " + address)
print("Bairro: " + neighborhood)
print("Cidade/Estado: " + state)

driver.quit()