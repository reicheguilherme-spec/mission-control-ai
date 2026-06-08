"""Motor de análise da Mission Control AI — AgroSat."""

import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

TRILHA = "agrosat"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md"""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de controle de missão espacial."

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao modelo via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        return client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"

class MissionEngine:
    """Motor de análise da missão AgroSat."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self):
        return True

    def status_snapshot(self):
        """Retorna resumo atual da telemetria."""
        dados = coletar()
        alertas, acoes = avaliar(dados)

        linhas = [
            "🛰️ STATUS DO AGROSAT-1",
            "─" * 40,
            f"🕐 Timestamp:          {dados['timestamp']}",
            f"🌿 Saúde NDVI:         {dados['ndvi_saude']}%",
            f"🌡️  Temperatura:        {dados['temperatura_payload']}°C",
            f"💾 Armazenamento:      {dados['armazenamento']}%",
            f"📡 Sinal Downlink:     {dados['sinal_downlink']}%",
            f"⚡ Energia:            {dados['energia']}%",
            f"🎯 Estab. Atitude:    {dados['estabilidade_atitude']}%",
            "─" * 40,
            "⚠️  ALERTAS:",
        ]

        for alerta in alertas:
            linhas.append(f"  {alerta}")

        if acoes:
            linhas.append("─" * 40)
            linhas.append("🤖 AÇÕES AUTOMÁTICAS:")
            for acao in acoes:
                linhas.append(f"  {acao}")

        return "\n".join(linhas)

    def analyze(self, pergunta_usuario):
        """Analisa a pergunta com base na telemetria + alertas + IA."""
        dados = coletar()
        alertas, acoes = avaliar(dados)

        alertas_texto = "\n".join(alertas)
        acoes_texto = "\n".join(acoes) if acoes else "Nenhuma ação automática necessária."

        prompt = f"""
Dados atuais de telemetria do AgroSat-1:
- Saúde do sensor NDVI: {dados['ndvi_saude']}%
- Temperatura do payload: {dados['temperatura_payload']}°C
- Armazenamento disponível: {dados['armazenamento']}%
- Sinal de downlink: {dados['sinal_downlink']}%
- Nível de energia: {dados['energia']}%
- Estabilidade de atitude: {dados['estabilidade_atitude']}%
- Timestamp: {dados['timestamp']}

Alertas detectados pelo sistema:
{alertas_texto}

Ações automáticas executadas:
{acoes_texto}

Pergunta do operador: {pergunta_usuario}

Responda como ARIA, a IA de controle de missão do AgroSat-1, conectando sempre a análise técnica ao impacto no agronegócio brasileiro.
"""
        return llm(prompt, system=self.system_prompt)