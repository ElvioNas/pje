from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações básicas do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Inicializa o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

#driver.find_element(By.ID, "element_id")
#driver.find_element(By.NAME, "element_name")
#driver.find_element(By.CLASS_NAME, "class_name")
#driver.find_element(By.TAG_NAME, "tag")
#driver.find_element(By.LINK_TEXT, "Texto do Link")
#driver.find_element(By.PARTIAL_LINK_TEXT, "Parte do Texto")
#driver.find_element(By.CSS_SELECTOR, "css.selector")
#driver.find_element(By.XPATH, "//div[@id='example']")
time.sleep(2)

#Realizando Login no sistema#

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("tjpe1917")
time.sleep(1)
driver.find_element(By.ID, "kc-login").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Configuração')]").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Motivos de Isenção").click()
driver.find_element(By.XPATH, "//label[contains(text(), 'Motivo de Isenção da Guia de Recolhimento')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Situação')]")
time.sleep(1)
driver.find_element(By.XPATH, "//td[contains(text(), 'Formulário')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'Campos obrigatórios')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Motivo de Isenção da Guia de Recolhimento')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Controla situação da guia')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Situação')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Sim')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Não')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Ativo')]")
time.sleep(1)
driver.find_element(By.XPATH, "//label[contains(text(), 'Inativo')]")
time.sleep(1)


#driver.find_element(
#    By.XPATH,
#    "//a[contains(normalize-space(), 'Audiências e sessões')]"
#).click()

time.sleep(1000)