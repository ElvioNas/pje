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

def contar(by, valor, acao=None, texto=None):
    global contador, sucessos, falhas
    contador += 1
    try:
        elemento = driver.find_element(by, valor)
        
        if acao == "click":
            elemento.click()
        elif acao == "send_keys":
            elemento.send_keys(texto)
            
        sucessos += 1
        print(f"[{contador}] ✔ OK -> {valor}")
        return elemento
        
    except Exception:
        falhas += 1
        print(f"[{contador}] ✖ FALHOU -> {valor}")
        return None


# ==============================
# CONFIGURAÇÃO DO CHROME
# ==============================

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ==============================
# ACESSAR SITE
# ==============================

driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

time.sleep(2)

# ==============================
# LOGIN
# ==============================

contar(By.ID, "username", "send_keys", "02112357417")
time.sleep(2)

contar(By.ID, "password", "send_keys", "tjpe1917")
time.sleep(2)

contar(By.ID, "kc-login", "click")
time.sleep(1)

# ==============================
# MENU DOWNLOAD
# ==============================

contar(By.CLASS_NAME, "botao-menu", "click")
time.sleep(1)

contar(By.XPATH, "//a[contains(text(), 'Download')]", "click")
time.sleep(1)

# ==============================
# VALIDAÇÃO DOWNLOAD
# ==============================

contar(By.XPATH, "//a[contains(text(), 'Área de download')]")
time.sleep(1)

contar(By.XPATH, "//a[contains(text(), 'Área de download')]", "click")

# ==============================
# RESULTADO FINAL
# ==============================

print("\n==============================")
print(f"Total de passos: {contador}")
print(f"Sucessos: {sucessos}")
print(f"Falhas: {falhas}")

if contador > 0:
    taxa = (sucessos / contador) * 100
    print(f"Taxa de sucesso: {taxa:.1f}%")

print("==============================")

time.sleep(1000)