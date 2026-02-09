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
driver.find_element(By.PARTIAL_LINK_TEXT, "Pessoa").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Advogado')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Alteração de dados cadastrais')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Ente ou autoridade')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Assistentes de procuradoria/defensoria')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Conciliador')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Física')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Jurídica')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Jus Postulandi')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Magistrado')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Oficial de justiça')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Perito')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Procurador/Defensor')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Servidor')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Push')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Qualificação')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Tipo de pessoa')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Advogado')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Atuação do advogado')]")
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(), 'Confirmar credenciamento')]")
time.sleep(1)
#driver.find_element(By.CLASS_NAME, "Advogado").click()
#time.sleep(1)
#driver.find_element(By.XPATH, "//[contains(text(), 'Advogado')]").click()
#time.sleep(1)
#driver.find_element(By.XPATH, "//a[contains(normalize-space(), 'Advogado')]").click()
#By.XPATH, "//a[contains(normalize-space(), 'Advogado')]"



#driver.find_element(
#    By.XPATH,
#    "//a[contains(normalize-space(), 'Audiências e sessões')]"
#).click()

time.sleep(1000)