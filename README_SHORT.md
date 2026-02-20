# README (Resumo Rápido)

## Visão Geral

- `robo.py`: automação e integração com WhatsApp/plataforma de pedidos, leitura/escrita de Excel, gerenciamento de estoque, notificações (Telegram/Grupos), e monitoramento contínuo (`start`, `monitorar`, `iniciar_chrome_persistente`).
- `painel.py`: interface gráfica (CustomTkinter) para controlar o robô, visualizar/extrair fechamentos, gerenciar vales e estoque, ver logs e fazer backups. Entradas principais: `iniciar_robo`, `parar_robo`, `gerar_excel_fechamento`, `carregar_estoque`.

## Uso rápido

- Iniciar GUI (Windows): clique em `INICIAR_ROBO.bat`
- Linha de comando:
```bash
python painel.py
```

## Dependências principais
- Python 3.10+ recomendado
- Veja `requirements.txt` / `requirements_pinned.txt` para pacotes

## Notas
- Excel esperado: `Controle_Financeiro_DD-MM-YYYY.xlsx` com abas `EXTRATO DETALHADO` e opcional `PAGAMENTO_MOTOBOYS`.
- Para métricas e validação, rode `python teste_performance.py` e anexe a saída caso queira comprovar resultados.
