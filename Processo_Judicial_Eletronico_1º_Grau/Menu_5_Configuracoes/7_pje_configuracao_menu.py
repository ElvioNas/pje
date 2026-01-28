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

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("tjpe1917")
time.sleep(2)
driver.find_element(By.ID, "kc-login").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Configuração')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(), 'Ambiente')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Audiências e sessões')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Central de mandados')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Competência')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Controle de acesso')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Criminal')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Distribuição')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Documento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Mobile')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Jurisdição')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Órgão julgador')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Órgão julgador colegiado')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Órgão de representação')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Motivos de Isenção')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pessoa')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Serviços')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Requisitórios')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Procuradoria')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Sistema')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Tabelas básicas')]")


time.sleep(1000)