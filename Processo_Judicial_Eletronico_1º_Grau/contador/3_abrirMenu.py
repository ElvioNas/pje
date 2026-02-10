from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ==============================
# CONTADORES
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

# ==============================
# LOGIN
# ==============================

elemento = contar(By.ID, "username")
if elemento:
    elemento.send_keys("02112357417")

time.sleep(2)

elemento = contar(By.ID, "password")
if elemento:
    elemento.send_keys("tjpe1917")

time.sleep(2)

elemento = contar(By.ID, "kc-login")
if elemento:
    elemento.click()

time.sleep(2)

# ==============================
# Validando Label no Menu
# ==============================

elemento = contar(By.CLASS_NAME, "botao-menu")
if elemento:
    elemento.click()

contar(By.XPATH, "//a[contains(text(), 'Painel')]")
contar(By.XPATH, "//a[contains(text(), 'Processo')]")
contar(By.XPATH, "//a[contains(text(), 'Atividades')]")
contar(By.XPATH, "//a[contains(text(), 'Audiências e sessões')]")
contar(By.XPATH, "//a[contains(text(), 'Configuração')]")
contar(By.XPATH, "//a[contains(text(), 'Download')]")

# ==============================
# RESULTADO FINAL
# ==============================

print("\n==============================")
print("RELATÓRIO FINAL")
print("==============================")
print(f"Total de interações: {contador}")
print(f"Sucessos: {sucessos}")
print(f"Falhas: {falhas}")

if contador > 0:
    taxa = (sucessos / contador) * 100
    print(f"Taxa de sucesso: {taxa:.2f}%")

print("==============================")

time.sleep(1000)