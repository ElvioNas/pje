
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

################ Validando label tela principal ############################

elemento = driver.find_element(By.XPATH, "//span[contains(text(), 'Processo Judicial Eletrônico')]")
assert elemento.text == "Processo Judicial Eletrônico"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Formas de Acesso')]")
assert elemento.text == "Formas de Acesso"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Consulta Processual')]")
assert elemento.text == "Consulta Processual"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Push')]")
assert elemento.text == "Push"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Manuais')]")
assert elemento.text == "Manuais"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Fale Conosco')]")
assert elemento.text == "Fale Conosco"

elemento = driver.find_element(By.XPATH, "//p[contains(text(), 'Processo Judicial Eletrônico 1º Grau')]")
assert elemento.text == "Processo Judicial Eletrônico 1º Grau"

elemento = driver.find_element(By.XPATH, "//p[contains(text(), 'Poder Judiciário de Pernambuco')]")
assert elemento.text == "Poder Judiciário de Pernambuco"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Solicitar nova senha')]")
assert elemento.text == "Solicitar nova senha"

elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Saiba como obter o certificado digital')]")
assert elemento.text == "Saiba como obter o certificado digital"


time.sleep(2)

time.sleep(1000)
# Fecha o navegador (opcional)
#driver.quit()