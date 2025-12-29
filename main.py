import os
import sys
import time
import platform
import urllib.request
import urllib.parse
from datetime import datetime

# --- SEUS DADOS DO TELEGRAM ---
TELEGRAM_TOKEN = "COLE_SEU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = 00000000

# --- Tenta importar direto. Se falhar, mostra o erro real ---
try:
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
except ImportError as e:
    print("\nERRO CRÍTICO DE BIBLIOTECA:")
    print(f"{e}")
    print("\nParece que o Python não está achando o 'undetected_chromedriver'.")
    print("Tente rodar no terminal: pip install undetected-chromedriver selenium")
    input("Pressione Enter para fechar...")
    sys.exit()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def enviar_telegram(mensagem):
    if TELEGRAM_TOKEN == "COLE_SEU_TOKEN_AQUI": return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = urllib.parse.urlencode({'chat_id': TELEGRAM_CHAT_ID, 'text': mensagem})
        urllib.request.urlopen(f"{url}?{params}")
    except: pass

def tocar_som(url_site):
    print("\n🔔 MUDANÇA DETECTADA! 🔔")
    enviar_telegram(f"🚨 Site atualizou!\nLink: {url_site}\nHora: {datetime.now().strftime('%H:%M')}")
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        else:
            print('\a')
    except: pass

def main():
    limpar_tela()
    print("=== MONITOR UNIVERSAL (SEM LOOP) ===")
    
    url_alvo = input(">> Cole a URL do site: ").strip()
    
    print("\n--- MODO DE LEITURA ---")
    print("1. Monitorar a PÁGINA INTEIRA")
    print("2. Monitorar FÓRUM INTELIGENTE")
    modo = input(">> Escolha (1 ou 2): ").strip()
    
    while True:
        try:
            minutos = float(input("\n>> Minutos entre checagens? ").replace(',', '.'))
            if minutos > 0: break
        except: pass

    intervalo = minutos * 60
    print("\n[INICIANDO] O navegador vai abrir...")
    
    try:
        options = uc.ChromeOptions()
        # Tenta criar o navegador
        driver = uc.Chrome(options=options, use_subprocess=True)
    except Exception as e:
        print(f"\nERRO AO ABRIR CHROME: {e}")
        print("Dica: Verifique se seu Chrome está atualizado.")
        input("Enter para sair...")
        return

    try:
        driver.get(url_alvo)
        print("Aguardando 15 segundos...")
        time.sleep(15)

        def pegar_texto():
            if modo == '2':
                ids_comuns = ["posts", "messageList", "bg-main", "site-content", "content"]
                for id_tentativa in ids_comuns:
                    try: return driver.find_element(By.ID, id_tentativa).text
                    except: continue
                classes_comuns = ["message-inner", "post-content", "entry-content"]
                for class_tentativa in classes_comuns:
                    try: return driver.find_element(By.CLASS_NAME, class_tentativa).text
                    except: continue
            return driver.find_element(By.TAG_NAME, "body").text

        try:
            conteudo_anterior = pegar_texto()
        except:
            print("Erro ao ler site. Tente outro link.")
            return

        print(f"[{datetime.now().strftime('%H:%M')}] Monitorando...")
        enviar_telegram(f"🤖 Monitorando: {url_alvo}")

        while True:
            for i in range(int(intervalo), 0, -1):
                print(f"Próxima em {i}s...   ", end='\r')
                time.sleep(1)
            
            print(f"[{datetime.now().strftime('%H:%M')}] Verificando...             ", end='\r')
            
            try:
                driver.refresh()
                time.sleep(8)
                conteudo_atual = pegar_texto()

                if conteudo_atual != conteudo_anterior:
                    tocar_som(url_alvo)
                    print(f"\nAlteração detectada às {datetime.now().strftime('%H:%M')}")
                    conteudo_anterior = conteudo_atual
                    print("-" * 40)
            except Exception: pass

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        try: driver.quit()
        except: pass

if __name__ == "__main__":
    main()