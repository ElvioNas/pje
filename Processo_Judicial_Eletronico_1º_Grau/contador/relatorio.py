from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# ==============================
# VARIÁVEIS GLOBAIS
# ==============================

contador = 0
sucessos = 0
falhas = 0
resultados = []

# ==============================
# FUNÇÃO PRINCIPAL DE TESTE
# ==============================

def passo(nome, by, valor, acao=None, texto=None, esperar=2):
    global contador, sucessos, falhas
    
    contador += 1
    
    try:
        elemento = driver.find_element(by, valor)
        
        if acao == "click":
            elemento.click()
            
        elif acao == "send_keys":
            elemento.send_keys(texto)
        
        sucessos += 1
        
        status = "OK"
        print(f"[{contador}] ✔ {nome}")
        
    except Exception as e:
        
        falhas += 1
        
        status = "FALHOU"
        print(f"[{contador}] ✖ {nome}")
    
    resultados.append({
        "numero": contador,
        "nome": nome,
        "status": status
    })
    
    time.sleep(esperar)

# ==============================
# GERAR RELATÓRIO HTML
# ==============================

def gerar_relatorio():
    
    taxa = (sucessos / contador) * 100 if contador > 0 else 0
    
    html = f"""
    <html>
    <head>
        <title>Relatório de Teste</title>
        <style>
            body {{ font-family: Arial; }}
            .ok {{ color: green; }}
            .falhou {{ color: red; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; }}
        </style>
    </head>
    <body>
    
    <h2>Relatório de Automação PJE</h2>
    
    <p>Total: {contador}</p>
    <p class="ok">Sucessos: {sucessos}</p>
    <p class="falhou">Falhas: {falhas}</p>
    <p>Taxa de sucesso: {taxa:.1f}%</p>
    
    <table>
        <tr>
            <th>#</th>
            <th>Passo</th>
            <th>Status</th>
        </tr>
    """
    
    for r in resultados:
        
        cor = "ok" if r["status"] == "OK" else "falhou"
        
        html += f"""
        <tr>
            <td>{r["numero"]}</td>
            <td>{r["nome"]}</td>
            <td class="{cor}">{r["status"]}</td>
        </tr>
        """
    
    html += """
    </table>
    
    </body>
    </html>
    """
    
    with open("relatorio.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("\nRelatório gerado: relatorio.html")


# ==============================
# CONFIGURAÇÃO
# ==============================

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ==============================
# TESTE
# ==============================

driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")

passo("Preencher usuário", By.ID, "username", "send_keys", "02112357417")

passo("Preencher senha", By.ID, "password", "send_keys", "tjpe1917")

passo("Clicar login", By.ID, "kc-login", "click")

passo("Abrir menu", By.CLASS_NAME, "botao-menu", "click")

passo("Abrir Audiências", By.XPATH, "//a[contains(text(), 'Audiências e sessões')]", "click")

passo("Validar Acórdão", By.XPATH, "//a[contains(text(), 'Acórdão')]")

passo("Validar Cadastro sessão", By.XPATH, "//a[contains(text(), 'Cadastro de sessão de julgamento')]")

passo("Validar Decisão", By.XPATH, "//a[contains(text(), 'Decisão de julgamento')]")

passo("Validar Tipo julgamento", By.XPATH, "//a[contains(text(), 'Tipo de julgamento')]")

passo("Validar Parâmetro", By.XPATH, "//a[contains(text(), 'Parâmetro')]")

passo("Validar Pauta audiência", By.XPATH, "//a[contains(text(), 'Pauta de audiência')]")

# ==============================
# FINALIZAÇÃO
# ==============================

print("\n==============================")
print(f"Total: {contador}")
print(f"Sucessos: {sucessos}")
print(f"Falhas: {falhas}")
print("==============================")

gerar_relatorio()

time.sleep(5)

driver.quit()