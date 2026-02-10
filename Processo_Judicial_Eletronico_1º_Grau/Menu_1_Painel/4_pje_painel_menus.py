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

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("tjpe1917")
time.sleep(2)
driver.find_element(By.ID, "kc-login").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel')]").click()
time.sleep(2)
#driver.find_element(By.PARTIAL_LINK_TEXT, "Painel do representante processual").click()

driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do representante processual')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel de expedientes')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do usuário')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel de julgamento')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do magistrado na sessão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do oficial de justiça')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do perito')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do procurador na sessão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do membro da OAB na sessão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do usuário antigo')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Painel do secretário da sessão')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Quadro de avisos')]")
time.sleep(1000)