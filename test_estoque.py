import painel
import os
import json
from types import SimpleNamespace

def main():
    print("ARQUIVO_ESTOQUE:", painel.ARQUIVO_ESTOQUE)
    # Garantir ambiente limpo
    try:
        if os.path.exists(painel.ARQUIVO_ESTOQUE):
            os.remove(painel.ARQUIVO_ESTOQUE)
            print("Arquivo existente removido para teste.")
    except Exception as e:
        print("Erro ao remover arquivo existente:", e)

    # Testar carregar_estoque (deve retornar lista vazia se não existir)
    try:
        res = painel.PainelUltra.carregar_estoque(None)
        print("carregar_estoque() retornou:", res)
    except Exception as e:
        print("Erro em carregar_estoque():", e)

    # Testar salvar_estoque_disk
    sample = [{"nome": "TesteItem", "estoque_fisico": 7}]
    obj = SimpleNamespace(estoque_data=sample)
    try:
        painel.PainelUltra.salvar_estoque_disk(obj)
        print("salvar_estoque_disk() executado com sucesso.")
    except Exception as e:
        print("Erro em salvar_estoque_disk():", e)

    # Ler arquivo criado
    try:
        with open(painel.ARQUIVO_ESTOQUE, "r", encoding="utf-8") as f:
            dados = json.load(f)
        print("Conteúdo do arquivo:", dados)
    except Exception as e:
        print("Erro ao ler arquivo gerado:", e)

if __name__ == '__main__':
    main()
