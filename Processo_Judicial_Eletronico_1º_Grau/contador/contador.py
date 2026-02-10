from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ==============================
# CONTADORES
# ==============================

total_verificacoes = 0
sucessos = 0
falhas = 0

def verificar(by, valor):
    global total_verificacoes, sucessos, falhas
    total_verificacoes += 1
    try:
        elemento = driver.find_element(by, valor)
        sucessos += 1
        print(f"[{total_verificacoes}] ✔ OK -> {valor}")
        return elemento
    except Exception as e:
        falhas += 1
        print(f"[{total_verificacoes}] ✖ FALHA -> {valor}")
        return None


def verificar_e_clicar(by, valor):
    elemento = verificar(by, valor)
    if elemento:
        elemento.click()


def verificar_e_escrever(by, valor, texto):
    elemento = verificar(by, valor)
    if elemento:
        elemento.send_keys(texto)


# ==============================
# Configurações básicas do Chrome
# ==============================

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

time.sleep(2)

# ==============================
# LOGIN
# ==============================

verificar_e_escrever(By.ID, "username", "02112357417")
time.sleep(1)

verificar_e_escrever(By.ID, "password", "tjpe1917")
time.sleep(1)

verificar_e_clicar(By.ID, "kc-login")
time.sleep(1)

# ==============================
# NAVEGAÇÃO
# ==============================

verificar_e_clicar(By.CLASS_NAME, "botao-menu")
time.sleep(1)

verificar_e_clicar(By.XPATH, "//a[contains(text(), 'Configuração')]")
time.sleep(1)

verificar_e_clicar(By.PARTIAL_LINK_TEXT, "Criminal")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Legislação Penal')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Órgão do procedimento de origem')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Tipo de origem')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Tipo de recurso')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'unidadePrisional.menuText')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Tipo de procedimento de origem')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Tipo de suspensão')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Tipo Evento Criminal')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Medida Socioeducativa')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Motivo Extinção Medida Socioeducativa')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Motivo Retorno Evasão')]")
time.sleep(1)

verificar_e_clicar(By.XPATH, "//a[contains(text(), 'Legislação Penal')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Norma penal')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Tipo de pena')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Dispositivo da norma')]")
time.sleep(1)

verificar(By.XPATH, "//a[contains(text(), 'Legislação Penal')]")

# ==============================
# RELATÓRIO FINAL
# ==============================

print("\n==============================")
print("RELATÓRIO FINAL")
print("==============================")
print(f"Total de verificações: {total_verificacoes}")
print(f"Sucessos: {sucessos}")
print(f"Falhas: {falhas}")

if total_verificacoes > 0:
    taxa = (sucessos / total_verificacoes) * 100
    print(f"Taxa de sucesso: {taxa:.2f}%")

print("==============================")

time.sleep(1000)