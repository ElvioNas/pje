from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

# ==============================
# CONTADOR DE INTERAÇÕES
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

contar(By.XPATH, "//a[contains(text(), 'Atividades')]").click()
time.sleep(2)

# VALIDAÇÕES

contar(By.XPATH, "//a[contains(text(), 'Assinar documentos pendentes')]")
contar(By.XPATH, "//a[contains(text(), 'Avisos')]")
contar(By.XPATH, "//a[contains(text(), 'Consulta pessoa')]")
contar(By.XPATH, "//a[contains(text(), 'Criar relação pessoal')]")
contar(By.XPATH, "//a[contains(text(), 'Desunificar pessoas')]")
contar(By.XPATH, "//a[contains(text(), 'Distribuição de expediente')]")
contar(By.XPATH, "//a[contains(text(), 'Emitir certidão')]")
contar(By.XPATH, "//a[contains(text(), 'Impressão de documento em lote')]")
contar(By.XPATH, "//a[contains(text(), 'Pauta de perícia')]")
contar(By.XPATH, "//a[contains(text(), 'Redistribuição de expediente')]")
contar(By.XPATH, "//a[contains(text(), 'Registrar disponibilidade de perito')]")
contar(By.XPATH, "//a[contains(text(), 'Registrar indisponibilidade de perito')]")
contar(By.XPATH, "//a[contains(text(), 'Requisição de antecipação de pagamento do perito')]")
contar(By.XPATH, "//a[contains(text(), 'Elaborar RPV ou precatório')]")
contar(By.XPATH, "//a[contains(text(), 'Imprimir RPV e precatório')]")
contar(By.XPATH, "//a[contains(text(), 'Simular valor a compensar')]")
contar(By.XPATH, "//a[contains(text(), 'Solicitação de antecipação de pagamento de perícia')]")
contar(By.XPATH, "//a[contains(text(), 'Baixar arquivo de contatos para o SPE Escritório')]")

# ==============================
# RESULTADO FINAL
# ==============================

print("\n==============================")
print(f"Total de interações: {contador}")
print(f"Sucessos: {contador - falhas}")
print(f"Falhas: {falhas}")
print("==============================")

time.sleep(1000)