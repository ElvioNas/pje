from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ==============================
# CONTADOR
# ==============================

contador = 0
sucessos = 0
falhas = 0

def contar(by, valor):
    global contador, sucessos, falhas
    contador += 1
    try:
        elemento = driver.find_element(by, valor)
        sucessos += 1
        print(f"[{contador}] ✔ OK -> {valor}")
        return elemento
    except Exception as e:
        falhas += 1
        print(f"[{contador}] ✖ FALHOU -> {valor}")
        return None


# Configurações básicas do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Inicializa o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

time.sleep(2)

# LOGIN

contar(By.ID, "username").send_keys("02112357417")
time.sleep(2)

contar(By.ID, "password").send_keys("tjpe1917")
time.sleep(2)

contar(By.ID, "kc-login").click()
time.sleep(2)

# MENU

contar(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)

contar(By.XPATH, "//a[contains(text(), 'Painel')]").click()
time.sleep(2)

# VALIDAÇÕES DO PAINEL

contar(By.XPATH, "//a[contains(text(), 'Painel do representante processual')]")
contar(By.XPATH, "//a[contains(text(), 'Painel de expedientes')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do usuário')]")
contar(By.XPATH, "//a[contains(text(), 'Painel de julgamento')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do magistrado na sessão')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do oficial de justiça')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do perito')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do procurador na sessão')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do membro da OAB na sessão')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do usuário antigo')]")
contar(By.XPATH, "//a[contains(text(), 'Painel do secretário da sessão')]")
contar(By.XPATH, "//a[contains(text(), 'Quadro de avisos')]")

# ==============================
# RESULTADO FINAL
# ==============================

print("\n==============================")
print(f"Total de interações realizadas: {contador}")
print("==============================")

time.sleep(1000)