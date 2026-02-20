# 📑 GUIA DE NAVEGAÇÃO - ESTRUTURA DO ROBO.PY

## Mapa de Seções e Funções

### ✅ SEÇÃO 1: IMPORTS E CONFIGURA ÇÃOÇÃO
**Localização:** Linhas ~1-150  
**Responsabilidade:** Carregar dependências e constantes

```
- Imports (selenium, requests, pandas, openpyxl, etc)
- Constantes de configuração
- Status cancelados
- Variáveis globais
```

---

### ✅ SEÇÃO 2: FUNÇÕES AUXILIARES DE CAMINHO E ARQUIVO
**Localização:** Linhas ~150-300  
**Responsabilidade:** Operações básicas com filesystem

```
get_caminho_base()
get_caminho_excel()
get_data_operacional()
carregar_credenciais()
salvar_credenciais()
```

---

### ✅ SEÇÃO 3: GPS E LOCALIZAÇÃO
**Localização:** Linhas ~500-700  
**Responsabilidade:** Integração com Google Maps e GPS

```
preparar_gps_loja()
buscar_coordenadas_endereco(endereco)
calcular_distancia_rota(origem, destino)
```

---

### ✅ SEÇÃO 4: CHROME & NAVEGADOR WEB
**Localização:** Linhas ~1000-1200  
**Responsabilidade:** Automação de browser para ZÉ Delivery

```
iniciar_chrome_persistente()
enviar_mensagem_grupo(mensagem)
```

---

### ✅ SEÇÃO 5: API ZÉ DELIVERY
**Localização:** Linhas ~1250-1450  
**Responsabilidade:** Integração com API da plataforma

```
requisicao_segura(query)
traduzir_status(status_raw)
buscar_telefone(num)
buscar_todos_pedidos_excel_por_nome(nome_buscado)
consultar_api_direta()
```

---

### ✅ SEÇÃO 6: WHATSAPP READ & REPLY
**Localização:** Linhas ~1450-1600  
**Responsabilidade:** Leitura e resposta de mensagens WhatsApp

```
verificar_solicitacoes_whatsapp()
PRIMEIRA_LEITURA_FEITA (controle)
```

---

### ✅ SEÇÃO 7: HISTÓRICO & SINCRONIZAÇÃO
**Localização:** Linhas ~1640-1800  
**Responsabilidade:** Sincronizar pedidos do dia com Excel

```
buscar_historico_do_dia(limite_paginas=None)
```

---

### ✅ SEÇÃO 8: MONITORAMENTO
**Localização:** Linhas ~1830-1900  
**Responsabilidade:** Monitorar status de pedidos em tempo real

```
monitorar()
```

---

### ✅ SEÇÃO 9: INTEGRAÇÃO COM PAINEL
**Localização:** Linhas ~1945-2100  
**Responsabilidade:** Comunicação com painel.py via arquivos

```
imprimir_extrato_por_nome(nome_alvo, data_str)
processar_comando_painel()
```

---

### ✅ SEÇÃO 10: RELATÓRIOS E IMPRESSÃO
**Localização:** Linhas ~2100-2400  
**Responsabilidade:** Gerar recibos e relatórios

```
imprimir_recibo_garantia(dados_brutos)
imprimir_lote_continuo(pedidos)
imprimir_resumo_extrato()
gerar_relatorio_executivo()
processar_relatorio_canceladas(data_cancel=None)
fazer_barulho()
```

---

### ✅ SEÇÃO 11: TELEGRAM BOT
**Localização:** Linhas ~2450-3200  
**Responsabilidade:** Integração com Telegram para comandos

#### Inicialização e Utilitários
```
enviar_telegram(mensagem)
normalizar_comando(texto)
```

#### Verificação de Comandos
```
verificar_comandos_telegram()
```

#### Submétodos de Comandos (dentro de verificar_comandos_telegram):
- `/ajuda` - Menu de help
- `/status` - Status do robô
- `/resumo` - Relatório completo
- `/canceladas` - Pedidos cancelados
- `/imprimir` - Buscar e imprimir pedidos
- `/motos` - Entregadores na rua
- `/pendentes` - Fila de pedidos
- `/garantia` - Cálculo de fechamento
- `/estoque` - Status do inventário

---

### ✅ SEÇÃO 12: ROTINA DE FECHAMENTO
**Localização:** Linhas ~3200-3350  
**Responsabilidade:** Envio automático de relatórios

```
verificar_rotina_fechamento()
RELATORIO_ENVIADO_HOJE (flag)
```

---

### ✅ SEÇÃO 13: ALERTA DE ESTOQUE
**Localização:** Linhas ~3350-3450  
**Responsabilidade:** Monitorar quanto de estoque está baixo

```
verificar_estoque_critico()
carregar_estoque_seguro(caminho, tentativas, atraso)
salvar_estoque_seguro(estoque, caminho)
processar_baixa_estoque(itens_texto)
processar_estorno_estoque(itens_texto)
```

---

### ✅ SEÇÃO 14: INICIALIZAÇÃO PRINCIPAL
**Localização:** Linhas ~3500-3600  
**Responsabilidade:** Loop principal do robô

```
start()
```

---

## 🎯 Fluxos Principais

### Fluxo 1: Iniciação do Robô
```
start()
  ↓
carregar_credenciais()
carregar_motoboys_do_painel()
inicializar_excel_agora()
preparar_gps_loja()
iniciar_chrome_persistente()
buscar_historico_do_dia(limite_paginas=None)
enviar_telegram("🚀 ROBÔ INICIADO COM SUCESSO!")
  ↓
LOOP INFINITO:
  - monitorar()
  - verificar_solicitacoes_whatsapp()
  - processar_comando_painel()
  - verificar_comandos_telegram()
  - verificar_rotina_fechamento()
  - verificar_estoque_critico()
  - time.sleep(5)
```

### Fluxo 2: Sincronização de Dados
```
buscar_historico_do_dia()
  ↓
Pega pedidos da API
  ↓
Processa cada pedido:
  - Salva no Excel
  - Atualiza status em cache
  - Envia mensagem WhatsApp se necessário
  ↓
Envia resumo para Telegram
```

### Fluxo 3: Comando do Telegram
```
verificar_comandos_telegram()
  ↓
Recebe /comando
  ↓
Processa comando (switch gigante):
  - /imprimir → imprimir_extrato_por_nome()
  - /resumo → gerar_relatorio_executivo()
  - /motos → consultar quem está na rua
  - etc...
  ↓
Envia resposta via Telegram
```

### Fluxo 4: Comando do Painel
```
painel.py escreve em: comando_imprimir.txt
  ↓
robo.py lê processar_comando_painel()
  ↓
Processa comando
  ↓
Envia resultado de volta (via arquivo ou Telegram)
```

---

## 📊 Variáveis Globais Importantes

```python
# Autenticação
TELEGRAM_TOKEN              # Token do Telegram Bot
TOKEN_ATUAL                 # Token da API Zé (renovado a cada sessão)
CHROME_PERSISTENTE         # Instância do Chrome Selenium

# Cache de Dados
CACHE_NOMES_DO_DIA         # Nomes de motoboys/clientes do dia
CACHE_STATUS_PEDIDOS       # Status cache dos pedidos
pedidos_em_espera          # Dict de pedidos aguardando

# Estado do Sistema
PRIMEIRA_LEITURA_FEITA     # Flag de primeira sincronização
RELATORIO_ENVIADO_HOJE     # Flag de relatório enviado automaticamente
ULTIMO_ALERTA_ESTOQUE      # Timestamp do último alerta

# Configuração
ARQUIVO_COMANDO            # "comando_imprimir.txt"
ARQUIVO_ESTOQUE            # "estoque.json"
```

---

## 🔍 Referência de Funções por Propósito

### Para ler dados:
- `buscar_historico_do_dia()` - Histórico de pedidos
- `consultar_api_direta()` - Dados em tempo real da API
- `carregar_estoque_seguro()` - Ler arquivo de estoque

### Para integração com Painel:
- `processar_comando_painel()` - Ler arquivo de comando
- `imprimir_extrato_por_nome()` - Imprimir pedido específico
- `gerar_relatorio_executivo()` - Gerar resumo do dia

### Para integração com Telegram:
- `verificar_comandos_telegram()` - Processar comandos
- `enviar_telegram()` - Enviar mensagem

### Para monitoramento:
- `monitorar()` - Verificar status de pedidos
- `verificar_estoque_critico()` - Alertar estoque baixo
- `verificar_rotina_fechamento()` - Fechamento automático

### Para WhatsApp:
- `verificar_solicitacoes_whatsapp()` - Ler e responder mensagens

---

##  ⚠️ Pontos de Atenção

1. **API Token Expira:** Token é renovado a cada ciclo de `monitorar()`
2. **Arquivo está em uso:** Use `carregar_estoque_seguro()` com retry
3. **Pedidos duplicados:** Cache é mantido para evitar duplicação
4. **Impressora Térmica:** Integração local, verificar se está conectada

---

## 🚀 Para Adicionar Novo Comando Telegram

1. Localize `verificar_comandos_telegram()`
2. Adicione um novo elif antes do processamento final:

```python
elif comando in ["meunovo", "novo"]:
    resultado = minha_nova_funcao()
    enviar_telegram(resultado)
```

3. Crie a função auxiliar:

```python
def minha_nova_funcao():
    # sua lógica aqui
    return "Resultado"
```

---

## 📝 Logs Recomendados

Todo acesso a arquivo crítico deveria fazer print:
```python
print(f"📂 Tentando abrir: {arquivo}")
print(f"✅ Sucesso!")
print(f"❌ Erro: {e}")
```

---

**Gerado:** 13/02/2026  
**Versão robo.py:** Atual
