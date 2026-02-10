from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ==============================
# CONTADOR ESTILO CYPRESS
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
        
    except Exception as e:
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
# ACESSA O SITE
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
time.sleep(2)

# ==============================
# MENU
# ==============================

contar(By.CLASS_NAME, "botao-menu", "click")
time.sleep(2)

contar(By.XPATH, "//a[contains(text(), 'Audiências e sessões')]", "click")
time.sleep(2)

# ==============================
# VALIDAÇÕES
# ==============================

contar(By.XPATH, "//a[contains(text(), 'Acórdão')]")
contar(By.XPATH, "//a[contains(text(), 'Cadastro de sessão de julgamento')]")
contar(By.XPATH, "//a[contains(text(), 'Decisão de julgamento')]")
contar(By.XPATH, "//a[contains(text(), 'Tipo de julgamento')]")
contar(By.XPATH, "//a[contains(text(), 'Parâmetro')]")
contar(By.XPATH, "//a[contains(text(), 'Pauta de audiência')]")
contar(By.XPATH, "//a[contains(text(), 'Publicação de decisões em sessão / em mural')]")
contar(By.XPATH, "//a[contains(text(), 'Pendências da sessão de julgamento')]")
contar(By.XPATH, "//a[contains(text(), 'Processos pautados em sessão')]")
contar(By.XPATH, "//a[contains(text(), 'Relação de julgamento')]")
contar(By.XPATH, "//a[contains(text(), 'Pauta de julgamento')]")

# ==============================
# RESULTADO FINAL
# ==============================

print("\n==============================")
print(f"Total: {contador}")
print(f"✔ Sucessos: {sucessos}")
print(f"✖ Falhas: {falhas}")

if contador > 0:
    taxa = (sucessos / contador) * 100
    print(f"Taxa de sucesso: {taxa:.1f}%")

print("==============================")

time.sleep(1000)