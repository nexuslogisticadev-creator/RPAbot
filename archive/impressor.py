import sys
import os
import time
from datetime import datetime, timedelta
import unicodedata
import re

# Tenta importar bibliotecas necessárias
try:
    import win32print
    import win32api
    TEM_IMPRESSORA = True
except ImportError:
    TEM_IMPRESSORA = False
    print("⚠️ AVISO: Instale 'pywin32' para imprimir (pip install pywin32)")

try:
    import openpyxl
except ImportError:
    print("❌ ERRO: Instale 'openpyxl' (pip install openpyxl)")
    time.sleep(5)
    sys.exit()

# ================= COMANDOS TÉRMICOS (ESC/POS) =================
CMD_INIT = b"\x1b\x40"
CMD_CENTER = b"\x1b\x61\x01"
CMD_LEFT = b"\x1b\x61\x00"
CMD_BOLD_ON = b"\x1b\x45\x01"
CMD_BOLD_OFF = b"\x1b\x45\x00"
CMD_DOUBLE_H = b"\x1b\x21\x10"
CMD_NORMAL = b"\x1b\x21\x00"
CMD_CUT = b"\x1d\x56\x00"

ARQUIVO_COMANDO = 'comando_imprimir.txt' # Conectado ao Painel

# ================= FUNÇÕES AUXILIARES =================
def get_caminho_base():
    if getattr(sys, 'frozen', False): return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def normalizar_texto(texto):
    if not texto: return ""
    try:
        nfkd = unicodedata.normalize('NFKD', str(texto))
        t = "".join([c for c in nfkd if not unicodedata.combining(c)]).lower().strip()
        return t
    except: return str(texto).lower().strip()

def limpar_texto_busca(texto):
    t = normalizar_texto(texto)
    for p in ["imprimir", "pedido", ":"]: t = t.replace(p, "")
    return t.strip()

# ================= LÓGICA DE IMPRESSÃO =================
def enviar_para_impressora(buffer_bytes):
    if not TEM_IMPRESSORA:
        print("🚫 Sem driver de impressora detectado.")
        return
    try:
        impressora_padrao = win32print.GetDefaultPrinter()
        hPrinter = win32print.OpenPrinter(impressora_padrao)
        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1, ("Ticket_Ze", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, buffer_bytes)
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
        print("✅ Impressão enviada com sucesso.")
    except Exception as e:
        print(f"❌ Erro físico na impressão: {e}")

def buscar_e_imprimir_do_excel(termo_busca):
    # 1. Achar o arquivo de hoje
    agora = datetime.now()
    if agora.hour < 10: agora -= timedelta(days=1)
    data_str = agora.strftime('%d-%m-%Y')
    caminho = os.path.join(get_caminho_base(), f'Controle_Financeiro_{data_str}.xlsx')

    if not os.path.exists(caminho):
        print(f"❌ Planilha de hoje ({data_str}) não encontrada.")
        return

    print(f"🔎 Buscando '{termo_busca}' na planilha...")
    
    try:
        wb = openpyxl.load_workbook(caminho, data_only=True)
        ws = wb["EXTRATO DETALHADO"]
        termo_norm = limpar_texto_busca(termo_busca)
        
        pedidos_encontrados = []

        # 2. Varrer Excel
        for row in ws.iter_rows(min_row=2, values_only=True):
            if not row or not row[2]: continue # Pula linha vazia
            
            # Colunas: 0=Data, 1=Hora, 2=Numero, 3=Cliente, 4=Bairro, 5=Status, 6=Motoboy, 8=Valor, 9=Itens
            numero = str(row[2])
            cliente = str(row[3]) if row[3] else ""
            motoboy = str(row[6]) if row[6] else ""
            
            # Busca Inteligente (Pelo numero, nome cliente ou nome motoboy)
            if (termo_norm in normalizar_texto(numero) or 
                termo_norm in normalizar_texto(cliente) or 
                termo_norm in normalizar_texto(motoboy)):
                
                pedidos_encontrados.append({
                    'numero': numero,
                    'hora': str(row[1]),
                    'cliente': cliente,
                    'bairro': str(row[4]),
                    'valor': float(row[8]) if row[8] else 0.0,
                    'itens': str(row[9]) if len(row) > 9 and row[9] else ""
                })

        if not pedidos_encontrados:
            print("⚠️ Nenhum pedido encontrado com esse termo.")
            return

        # 3. Montar Ticket (Estilo Zé Delivery Compacto)
        print(f"🖨️ Encontrados {len(pedidos_encontrados)} pedidos. Imprimindo...")
        
        buffer = CMD_INIT + CMD_LEFT + CMD_BOLD_ON
        
        for i, p in enumerate(pedidos_encontrados):
            # Cabeçalho
            buffer += f"PED: {p['numero']}  |  {p['hora']}\n".encode('cp850', errors='ignore')
            buffer += f"CLI: {p['cliente'][:30]}\n".encode('cp850', errors='ignore')
            buffer += f"BAI: {p['bairro'][:30]}\n".encode('cp850', errors='ignore')
            
            # Itens
            if p['itens']:
                itens_limpo = p['itens'].replace("\n", " ").replace(" | ", " ")
                buffer += f"ITM: {itens_limpo[:45]}\n".encode('cp850', errors='ignore')
            
            # Valor
            buffer += f"$$$: R$ {p['valor']:.2f}\n".replace('.', ',').encode('cp850')
            
            # Separador
            if i < len(pedidos_encontrados) - 1:
                buffer += b"--------------------------------\n"
            else:
                buffer += b"\n\n\n" # Espaço final

        buffer += CMD_CUT
        enviar_para_impressora(buffer)

    except Exception as e:
        print(f"❌ Erro ao ler Excel: {e}")

# ================= LOOP PRINCIPAL =================
def vigiar_fila():
    print("="*40)
    print("🖨️  IMPRESSOR INTELIGENTE ATIVO")
    print(f"👀  Vigiando arquivo: {ARQUIVO_COMANDO}")
    print("="*40)
    
    while True:
        if os.path.exists(ARQUIVO_COMANDO):
            try:
                # 1. Ler o comando
                with open(ARQUIVO_COMANDO, 'r', encoding='utf-8') as f:
                    conteudo = f.read().strip()
                
                # 2. Apagar o arquivo (para não imprimir de novo)
                time.sleep(0.5)
                try: os.remove(ARQUIVO_COMANDO)
                except: pass

                if not conteudo: continue

                print(f"\n📩 Comando recebido: {conteudo}")

                # 3. Identificar tipo de comando
                if conteudo.startswith("IMPRIMIR:"):
                    termo = conteudo.replace("IMPRIMIR:", "").strip()
                    if "|" in termo: termo = termo.split("|")[0] # Remove data se vier junto
                    buscar_e_imprimir_do_excel(termo)
                else:
                    # Se for algo genérico, tenta buscar igual
                    buscar_e_imprimir_do_excel(conteudo)

            except Exception as e:
                print(f"❌ Erro no loop: {e}")
        
        time.sleep(1.5)

if __name__ == "__main__":
    vigiar_fila()