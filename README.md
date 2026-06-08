# 🚀 Mission Control AI — AgroSat

## 👥 Integrantes
- Guilherme Reiche — RM: 569918 — Turma: 1CCPG
- Enzo Guislandi — RM: 569885 — Turma: 1CCPG
- Nicolas Nishi — RM: 572242 — Turma: 1CCPG

## 📋 O que o projeto faz
O AgroSat Mission Control AI é um sistema de monitoramento operacional de satélite de sensoriamento agrícola. O sistema simula dados de telemetria do satélite AgroSat-1, detecta anomalias automaticamente via lógica Python e utiliza IA generativa (ARIA) para analisar o estado da missão em linguagem natural, conectando cada decisão técnica orbital ao impacto no agronegócio brasileiro.

## 🎭 Persona atendida
**Engenheiro de operações do AgroSat-1** — profissional responsável por monitorar a saúde do satélite em tempo real e tomar decisões rápidas quando parâmetros saem do normal. O sistema traduz dados técnicos complexos em linguagem acessível, permitindo que o operador entenda rapidamente o impacto de cada anomalia para os produtores rurais que dependem dos dados do satélite.

## 🛠️ Tecnologias utilizadas
- Python 3.10+
- Ollama Cloud API (modelo gpt-oss:120b)
- Rich 15.0.0 (interface visual no terminal)
- Prompt Toolkit 3.0.52 (input interativo)
- PyFiglet 1.0.4 (banner ASCII)
- Python-dotenv 1.2.2 (variáveis de ambiente)

## ▶️ Como executar

1. Clone o repositório
```bash
git clone https://github.com/seuusuario/mission-control-ai
cd mission-control-ai
```

2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` na raiz com sua chave Ollama
5. Execute o sistema
```bash
python main.py
```

## 🖥️ Demonstração

![Banner e interface do sistema](assets/screenshot_banner.png)
![IA analisando dados da missão](assets/screenshot_analise.png)

## 🧠 System Prompt
O system prompt completo está em [`prompts/system_prompt.md`](prompts/system_prompt.md). A IA assume a persona de ARIA (Agricultural Remote Intelligence Assistant), sempre conectando análise técnica ao impacto no agronegócio brasileiro.

## 🧪 Cenários de teste demonstrados
1. **Operação normal** — todos os parâmetros dentro do range esperado
2. **Energia crítica** — bateria abaixo de 20%, modo economia ativado automaticamente
3. **Sinal fraco** — downlink abaixo de 50%, tentativa de reconexão automática
4. **Sensor NDVI degradado** — diagnóstico automático iniciado

## ⚠️ Limitações conhecidas
- Os dados de telemetria são simulados aleatoriamente, não refletem um satélite real
- O sistema não possui memória entre sessões — cada execução começa do zero
- A qualidade das respostas da IA depende da disponibilidade do Ollama Cloud

## 💼 Proposta de valor / modelo de negócio

**1. Problema real terrestre que esta missão resolve:**
O agronegócio brasileiro depende cada vez mais de dados de sensoriamento remoto para decisões de irrigação, aplicação de defensivos e acionamento de seguros rurais. Quando um satélite falha ou opera degradado, milhares de produtores perdem acesso a dados críticos, resultando em perdas de produtividade e decisões equivocadas.

**2. Quem paga pela solução:**
Modelo híbrido — setor privado (cooperativas agrícolas, seguradoras rurais, plataformas como Climate FieldView) paga por acesso aos dados via API, enquanto o setor público (Embrapa, MAPA) subsidia o acesso para pequenos produtores.

**3. Métrica de impacto:**
Se o AgroSat-1 operar 100% saudável por 1 ano, aproximadamente 15.000 produtores rurais do Centro-Oeste e Sul do Brasil terão acesso a imagens NDVI diárias, permitindo monitoramento de cerca de 2 milhões de hectares de lavoura, reduzindo perdas estimadas em 18% por decisões tardias de irrigação.

**4. Modelo de negócio:**
Dado-como-serviço (DaaS) — operadoras e plataformas agrícolas assinam acesso à API de imagens e análises do AgroSat-1 por hectare monitorado por mês.

## 🎬 Vídeo de demonstração
🔗 [Assistir demonstração no YouTube](https://youtu.be/A5e6_2e3gr8)
> Configurado como "Não listado" no YouTube.