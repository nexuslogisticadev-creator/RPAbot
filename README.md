# 🤖 Ze Bot - Automação Logística e Monitoramento

Bem-vindo ao repositório do **Ze Bot**, uma solução de automação focada em otimizar a triagem de pedidos operacionais, gestão financeira de motoboys e o monitoramento logístico em tempo real.

![Demonstração do Bot em funcionamento](demonstracao-bot.gif)

## 🎯 O Problema
Na operação logística de entregas rápidas, o processamento manual de dados de pedidos e a falta de alertas em tempo real geram gargalos no tempo de resposta, impactando diretamente o SLA (Service Level Agreement) e aumentando a chance de erros humanos no rastreio e no acerto financeiro dos entregadores.

## 💡 A Solução (Arquitetura do Sistema)
O Ze Bot atua como um sistema completo, dividido em duas camadas principais:

### 1. O Motor Backend (`robo.py`)
* **Processamento e Integração:** Automação web persistente com Chrome, integração com WhatsApp/Zé Delivery.
* **Gestão de Dados:** Leitura, escrita e inicialização automática de planilhas Excel (`Controle_Financeiro_DD-MM-YYYY.xlsx`).
* **Estoque e Alertas:** Gerenciamento de baixas/estornos de estoque e disparo de notificações automáticas via Telegram e grupos (`enviar_telegram()`).
* **Resiliência:** Funções de retry/timeout (`requisicao_segura()`) e monitoramento contínuo.

### 2. O Painel de Controle Frontend (`painel.py`)
Interface gráfica desenvolvida com CustomTkinter para gestão total da operação:
* Controle do robô (Start/Stop) e visualização de logs em tempo real.
* Gestão de estoque e adição manual de vales/descontos para motoboys.
* Cálculo automatizado de fechamento financeiro e exportação de relatórios.
* Sistema de backup integrado das configurações.

## 🚀 Otimizações de Performance (v1.0)
O sistema passou por uma refatoração profunda para garantir alta eficiência operacional. O painel agora é **70-90% mais rápido**.

| Métrica | Antes | Depois | Melhoria |
|---------|-------|--------|----------|
| **Tempo de leitura** | 27ms | 16ms | **1.7x** ⬆️ |
| **Recarregamentos** | 60/min | 10/min | **80%** ⬇️ |
| **CPU (ocioso)** | 8-15% | 0.5-2% | **90%** ⬇️ |
| **RAM usada** | 600MB | 350MB | **42%** ⬇️ |
| **Resposta da UI** | 500ms+ | <100ms | **5x** ⬆️ |

**Principais Implementações Técnicas:**
* **Verificação Inteligente (mtime):** O sistema só recarrega os dados se o arquivo Excel sofrer alterações, economizando 80% dos recarregamentos.
* **Leitura Seletiva (Pandas Cache):** Uso do Pandas (2.8x mais rápido que openpyxl) carregando apenas as colunas estritamente necessárias na memória.
* **Auto-Refresh Inteligente e Thread-Safe:** Verificação a cada 2 segundos via fila de eventos (Queue), evitando travamentos na interface (Sem Race Conditions ou Deadlocks).
* **Renderização Otimizada:** O componente TreeView foi reescrito para evitar loops vazios, garantindo fluidez instantânea.

## 🛠️ Tecnologias Utilizadas
* **Linguagem Principal:** Python 3.10+
* **Interface Gráfica (GUI):** CustomTkinter
* **Web Scraping & Automação Web:** Selenium (WebDriver persistente)
* **Manipulação de Dados:** Pandas & Openpyxl (Fallback)
* **Integrações:** APIs REST, Telegram, WhatsApp

## ⚙️ Como executar este projeto localmente

> **Aviso de Privacidade:** Por motivos de segurança (LGPD), este repositório serve como um portfólio demonstrativo. Credenciais reais, tokens e dados sensíveis foram removidos.

1. Clone o repositório:
```bash
git clone [https://github.com/nexuslogisticadev-creator/portfolio-zebot.git](https://github.com/nexuslogisticadev-creator/portfolio-zebot.git)
```
2.Instale as dependências:
```Bash
pip install -r requirements.txt
```
3. Execute a aplicação:

Via Interface Windows (Script): Clique no arquivo INICIAR_ROBO.bat e depois de abrir o painel clicar em iniciar sistema.

Via Terminal (Para Desenvolvedores): Execute o comando python painel.py e depois clicar em iniciar sistema.

4. Geração Automática do Banco de Dados:
Ao iniciar a aplicação, o motor do robô chamará a função inicializar_excel_agora(), que criará automaticamente o arquivo base (Controle_Financeiro_DD-MM-YYYY.xlsx) estruturando do zero todas as abas (EXTRATO DETALHADO, PAGAMENTO_MOTOBOYS) e colunas necessárias para o dia.

5. Testes e Validação:
Para comprovar as métricas de leitura e performance localmente, execute python teste_performance.py ou python validar_ambiente.py.

**Desenvolvido por Adiel Alves**  
**Data:** 20 de Fevereiro de 2026  
**Versão:** 1.0 Otimizada  
**Status:** ✅ Produção
