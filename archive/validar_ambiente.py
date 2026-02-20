#!/usr/bin/env python3
"""
Script de teste rápido - Valida que o painel está funcionando com as otimizações
"""

import os
import sys
import time
from datetime import datetime, timedelta

def get_caminho_base():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def get_data_operacional():
    agora = datetime.now()
    if agora.hour < 10:
        agora -= timedelta(days=1)
    return agora.strftime("%d-%m-%Y")

def verificar_arquivo_excel():
    """Verifica se arquivo Excel existe"""
    print("📋 VERIFICANDO ARQUIVO EXCEL")
    print("-" * 60)
    
    data = get_data_operacional()
    arq = os.path.join(get_caminho_base(), f"Controle_Financeiro_{data}.xlsx")
    
    if os.path.exists(arq):
        tamanho = os.path.getsize(arq) / 1024  # KB
        mtime = os.path.getmtime(arq)
        mtime_str = datetime.fromtimestamp(mtime).strftime("%d/%m/%Y %H:%M:%S")
        
        print(f"✅ Arquivo encontrado: {arq}")
        print(f"📊 Tamanho: {tamanho:.1f} KB")
        print(f"⏱️  Última modificação: {mtime_str}")
        return True
    else:
        print(f"❌ Arquivo não encontrado: {arq}")
        print(f"   Criar um Excel com os dados para testar")
        return False

def verificar_imports():
    """Verifica se todas as bibliotecas necessárias estão instaladas"""
    print("\n📚 VERIFICANDO IMPORTS")
    print("-" * 60)
    
    imports_obrigatorios = [
        ('pandas', 'pd'),
        ('openpyxl', 'openpyxl'),
        ('customtkinter', 'ctk'),
        ('tkinter', 'tk'),
    ]
    
    imports_opcionais = [
        ('matplotlib', 'matplotlib'),
        ('folium', 'folium'),
        ('gspread', 'gspread'),
        ('tkcalendar', 'tkcalendar'),
    ]
    
    print("Obrigatórios:")
    for nome, import_name in imports_obrigatorios:
        try:
            __import__(import_name)
            print(f"  ✅ {nome}")
        except ImportError:
            print(f"  ❌ {nome} - INSTALE: pip install {nome}")
    
    print("\nOpcionais:")
    for nome, import_name in imports_opcionais:
        try:
            __import__(import_name)
            print(f"  ✅ {nome}")
        except ImportError:
            print(f"  ⚠️  {nome} (não obrigatório)")

def check_config():
    """Verifica arquivo de configuração"""
    print("\n⚙️  VERIFICANDO CONFIG")
    print("-" * 60)
    
    config_path = os.path.join(get_caminho_base(), "config.json")
    
    if os.path.exists(config_path):
        tamanho = os.path.getsize(config_path)
        print(f"✅ config.json encontrado ({tamanho} bytes)")
        return True
    else:
        print(f"⚠️  config.json não encontrado")
        print(f"   Será criado automaticamente ao abrir o painel")
        return False

def testar_mtime():
    """Testa se mtime check vai funcionar"""
    print("\n📅 TESTANDO MTIME CHECK")
    print("-" * 60)
    
    data = get_data_operacional()
    arq = os.path.join(get_caminho_base(), f"Controle_Financeiro_{data}.xlsx")
    
    if not os.path.exists(arq):
        print("❌ Arquivo não existe, pulando teste")
        return
    
    try:
        mtime1 = os.path.getmtime(arq)
        time.sleep(0.5)
        mtime2 = os.path.getmtime(arq)
        
        if mtime1 == mtime2:
            print("✅ Mtime check funcionando (arquivo não mudou)")
        else:
            print("⚠️  Arquivo foi modificado, mtime é diferente")
    except Exception as e:
        print(f"❌ Erro: {e}")

def main():
    print("=" * 60)
    print("🔍 VALIDAÇÃO PRÉ-EXECUÇÃO DO PAINEL")
    print("=" * 60)
    
    verificar_arquivo_excel()
    verificar_imports()
    check_config()
    testar_mtime()
    
    print("\n" + "=" * 60)
    print("✅ VALIDAÇÃO COMPLETA")
    print("=" * 60)
    print("\n🚀 Próximo passo: Execute 'python painel.py' ou clique em INICIAR_ROBO.bat")

if __name__ == "__main__":
    main()
