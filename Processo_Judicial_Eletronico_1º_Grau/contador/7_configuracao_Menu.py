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
time.sleep(2)

# ==============================
# MENU
# ==============================

contar(By.CLASS_NAME, "botao-menu", "click")
time.sleep(2)

contar(By.XPATH, "//a[contains(text(), 'Configuração')]", "click")
time.sleep(2)

# ==============================
# VALIDAÇÕES
# ==============================

contar(By.XPATH, "//a[contains(text(), 'Ambiente')]")
contar(By.XPATH, "//a[contains(text(), 'Audiências e sessões')]")
contar(By.XPATH, "//a[contains(text(), 'Central de mandados')]")
contar(By.XPATH, "//a[contains(text(), 'Competência')]")
contar(By.XPATH, "//a[contains(text(), 'Controle de acesso')]")
contar(By.XPATH, "//a[contains(text(), 'Criminal')]")
contar(By.XPATH, "//a[contains(text(), 'Distribuição')]")
contar(By.XPATH, "//a[contains(text(), 'Documento')]")
contar(By.XPATH, "//a[contains(text(), 'Mobile')]")
contar(By.XPATH, "//a[contains(text(), 'Jurisdição')]")
contar(By.XPATH, "//a[contains(text(), 'Órgão julgador')]")
contar(By.XPATH, "//a[contains(text(), 'Órgão julgador colegiado')]")
contar(By.XPATH, "//a[contains(text(), 'Órgão de representação')]")
contar(By.XPATH, "//a[contains(text(), 'Motivos de Isenção')]")
contar(By.XPATH, "//a[contains(text(), 'Pessoa')]")
contar(By.XPATH, "//a[contains(text(), 'Serviços')]")
contar(By.XPATH, "//a[contains(text(), 'Requisitórios')]")
contar(By.XPATH, "//a[contains(text(), 'Procuradoria')]")
contar(By.XPATH, "//a[contains(text(), 'Sistema')]")
contar(By.XPATH, "//a[contains(text(), 'Tabelas básicas')]")
contar(By.XPATH, "//a[contains(text(), 'Tabelas judiciais')]")
contar(By.XPATH, "//a[contains(text(), 'AJG')]")
contar(By.XPATH, "//a[contains(text(), 'Autos Digitais')]")

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