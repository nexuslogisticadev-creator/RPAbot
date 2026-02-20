# 📑 GUIA DE NAVEGAÇÃO - ESTRUTURA DO PAINEL.PY

## Mapa Rápido de Métodos por Seção

### ✅ SEÇÃO 1: INICIALIZAÇÃO E EVENTOS DO SISTEMA
**Localização:** Linhas ~280-320  
**Responsabilidade:** Inicializar aplicação e gerenciar ciclo de vida

```
_post_init_load()
_auto_refresh_inteligente()
_maximize_window()
_force_zoom_once(event=None)
_on_unmap(event=None)
_on_map_refresh(event=None)
_on_resize(event)
_apply_resize(w)
_set_loading(active)
```

---

### ✅ SEÇÃO 2: LAYOUT E INTERFACE
**Localização:** Linhas ~374-651  
**Responsabilidade:** Construir e gerenciar menu lateral e tabs

```
criar_menu_lateral()
criar_botao_menu(texto, aba, row)
criar_area_principal()
_toggle_sidebar()
mudar_aba(nome_aba)
criar_card_stat(parent, titulo, valor, cor, col_idx)
criar_tabela_dark(parent, colunas)
```

---

### ✅ SEÇÃO 3: ABA FECHAMENTO
**Localização:** Linhas ~667-1280  
**Responsabilidade:** Cálculo de produção vs garantia para pagamento

#### Setup e Dados
```
setup_aba_fechamento(parent)
atualizar_dados_fechamento()
_carregar_dados_fechamento()
```

#### Renderização
```
_render_fechamento(dados)
_limpar_fechamento_tabela()
_montar_cabecalho_fechamento()
_criar_linha_fechamento(nome, info)
```

#### Cálculos e Utilitários
```
_parse_float(texto)
_parse_hora(texto)
_calcular_garantia_valor(t_in, t_out)
_recalcular_fechamento_linha(nome, mostrar_erros)
calcular_fechamento_todos()
```

#### Motoboys e Integração
```
_obter_pix_motoboy(nome)
_copiar_pix_motoboy(nome)
obter_motoboys_disponiveis()
atualizar_lista_motoboys_vales()
calcular_total_vales_moto(nome)
```

#### Google Sheets
```
_carregar_google_sheets_config()
_obter_nome_aba_sheets()
gerar_excel_fechamento()
```

---

### ✅ SEÇÃO 4: ABA MONITOR & DASHBOARD
**Localização:** Linhas ~1348-1446  
**Responsabilidade:** Exibir pedidos do dia com filtros e buscas

```
setup_aba_monitor(parent)
```

---

### ✅ SEÇÃO 5: ABA VALES & DESCONTOS
**Localização:** Linhas ~1449-1635  
**Responsabilidade:** Gerenciar descontos/vales para motoboys

```
setup_aba_vales(parent)
carregar_tabela_vales()
_render_vales(data)
adicionar_vale_manual()
excluir_vale()
editar_vale()
```

---

### ✅ SEÇÃO 6: ABA ESTOQUE
**Localização:** Linhas ~1640-1933  
**Responsabilidade:** Gerenciar inventário de produtos

```
setup_aba_estoque(parent)
carregar_estoque()
salvar_estoque_disk()
add_produto()
del_produto()
atualizar_tabela_estoque(filtro="")
gerar_barra_visual(atual, maximo=100)
identificar_categoria(nome_produto)
gerar_lista_compras()
```

---

### ✅ SEÇÃO 7: ABA BI & MAPAS
**Localização:** Linhas ~1939-1972  
**Responsabilidade:** Exibir gráficos e análises

```
setup_aba_bi(parent)
atualizar_graficos_bi()
gerar_mapa_calor()
```

---

### ✅ SEÇÃO 8: ABA CONFIG, LOGS, MOTOS E BAIRROS
**Localização:** Linhas ~1975-2135  
**Responsabilidade:** Configuração, logs, equipe e zones

```
# Configuração
setup_aba_config(parent)
salvar_creds()
selecionar_pasta_backup()
fazer_backup()

# Logs
setup_aba_logs(parent)

# Motos/Equipe
setup_aba_motos(parent)
atualizar_lista_motos()
add_moto()
del_moto()
salvar_motos_disk()

# Bairros/Zonas
setup_aba_bairros(parent)
atualizar_listas_bairros()
add_bairro(v)
del_bairro(v)
salvar_bairros_disk()
```

---

### ✅ SEÇÃO 9: SISTEMA DE ROBÔ
**Localização:** Linhas ~2157-2304  
**Responsabilidade:** Integração com robô externo

```
buscar_robo_no_sistema()
controlar_janela(acao)
toggle_robo()
iniciar_robo()
parar_robo()
```

---

### ✅ SEÇÃO 10: LOGS & TERMINAL
**Localização:** Linhas ~2257-2306  
**Responsabilidade:** Exibir logs do sistema em tempo real

```
iniciar_tail_log()
ler_log_arquivo()
ler_output_robo()
atualizar_logs_interface()
enviar_comando_robo()
log_sistema(msg)
```

---

### ✅ SEÇÃO 11: CONFIGURAÇÃO & ARQUIVOS
**Localização:** Linhas ~2309-2351  
**Responsabilidade:** Carregar/salvar configurações

```
carregar_config()
salvar_config()
atualizar_cache_bairros()
```

---

### ✅ SEÇÃO 12: CACHE & EXCEL
**Localização:** Linhas ~2354-2590  
**Responsabilidade:** Ler dados do Excel com cache inteligente

```
invalidar_cache_excel()
carregar_excel_cache(arq)
carregar_vales_cache(arq)
_excel_path(data_str=None)
carregar_tabela(filtro=None)
_coletar_dados_tabela(arq, filtro)
_render_tabela(data)
```

---

### ✅ SEÇÃO 13: MONITOR & FILTROS
**Localização:** Linhas ~2644-2788  
**Responsabilidade:** Busca, filtro e edição de pedidos

```
filtrar_tabela_busca(event)
ao_clicar_duas_vezes_pedido(event)
salvar_alteracao_excel(numero_pedido, novos_dados)
imprimir_combo_motoboy()
enviar_canceladas()
enviar_print()
mostrar_toast(mensagem, tipo="info")
```

---

### ✅ SEÇÃO 14: UI QUEUE (THREAD-SAFE)
**Localização:** Linhas ~2138-2155  
**Responsabilidade:** Garantir segurança de thread na UI

```
_enqueue_ui(fn)
_process_ui_queue()
```

---

## 🎯 Dicas de Navegação

### Para encontrar uma funcionalidade:

1. **Procurando edição de pedidos?**
   → Seção 4 (Monitor) ou Seção 13 (Filtros/Edição)

2. **Procurando cálculo de pagamento?**
   → Seção 3 (Fechamento)

3. **Procurando gestão de estoque?**
   → Seção 6 (Estoque)

4. **Procurando leitura do Excel?**
   → Seção 12 (Cache & Excel)

5. **Procurando integração com robô?**
   → Seção 9 (Sistema de Robô) + Seção 10 (Logs)

6. **Procurando layout/interface?**
   → Seção 2 (Layout e Interface)

---

##  🔍 Referência Cruzada

| Tarefa | Seção | Método |
|--------|-------|--------|
| Carregar dados do Excel | 12 | `carregar_excel_cache()` |
| Atualizar dashboard | 4 | `setup_aba_monitor()` |
| Calcular fechamento | 3 | `calcular_fechamento_todos()` |
| Adicionar vale | 5 | `adicionar_vale_manual()` |
| Recarregar dados automaticamente | 1 | `_auto_refresh_inteligente()` |
| Adicionar novo motoboy | 8 | `add_moto()` |
| Gerar relatório Excel | 3 | `gerar_excel_fechamento()` |
| Gerenciar logs | 10 | `atualizar_logs_interface()` |

---

## 📝 Ordem de Execução Típica

Ao abrir o painel:

1. **`__init__` (Seção 1)** → Inicializa todo o painel
2. **`_post_init_load` (Seção 1)** → Carrega dados iniciais
3. **`mudar_aba` (Seção 2)** → Muda para tab "monitor"
4. **`carregar_tabela` (Seção 4)** → Carrega pedidos do Excel
5. **`_coletar_dados_tabela` (Seção 12)** → Lê dados em background
6. **`_enqueue_ui` (Seção 14)** → Enfileira renderização segura
7. **`_render_tabela` (Seção 12)** → Renderiza pedidos na UI
8. **`_auto_refresh_inteligente` (Seção 1)** → Monitora mudanças a cada 2s

---

## 🚀 Para Adicionar Nova Aba

1. Crie a função `setup_aba_nova(parent)` logisticamente perto de outras abas (ex: Seção 8)
2. Adicione o call em `criar_area_principal()` 
3. Crie a entrada do botão em `criar_botao_menu()`
4. Integre em `mudar_aba()` se precisar carregar dados
5. Use `_enqueue_ui()` para operações HTTP/arquivo se necessário

---

**Gerado:** 13/02/2026  
**Versão painel.py:** 8.0 Organizado
