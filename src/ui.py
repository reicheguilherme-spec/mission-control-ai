"""Interface CLI estilo Claude Code — AgroSat Mission Control."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))

def show_banner():
    """Exibe banner ASCII colorido no início."""
    linha1 = pyfiglet.figlet_format("AgroSat", font="ansi_shadow")
    linha2 = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")

    console.print(Text(linha1, style="bold #A855F7"))
    console.print(Text(linha2, style="bold #06B6D4"))
    console.print(Text(
        "── 2026.1 · FIAP · Prompt Engineering and AI ──\n",
        style="italic #8484A0"
    ))

    tabela = Table(show_header=False, border_style="#06B6D4", expand=False)
    tabela.add_column("comando", style="#06B6D4")
    tabela.add_column("descrição", style="white")
    tabela.add_row("/status", "Ver telemetria atual do satélite")
    tabela.add_row("/help",   "Ver todos os comandos disponíveis")
    tabela.add_row("/about",  "Sobre o projeto")
    tabela.add_row("/clear",  "Limpar a tela")
    tabela.add_row("/exit",   "Encerrar o sistema")

    console.print(Panel(
        tabela,
        title="🛰️  AGROSAT-1 · Mission Control AI",
        subtitle="Modelo: gpt-oss:120b via Ollama Cloud",
        border_style="#06B6D4"
    ))

def show_response(text):
    """Renderiza resposta da IA em painel com timestamp."""
    now = datetime.now().strftime("%H:%M:%S")
    console.print(Panel(
        text,
        title="🤖 ARIA — Agricultural Remote Intelligence Assistant",
        subtitle=now,
        border_style="#A855F7"
    ))

def show_about():
    """Exibe informações sobre o projeto."""
    console.print(Panel(
        "🌾 [bold]AgroSat Mission Control AI[/bold]\n\n"
        "Sistema de monitoramento de satélite de sensoriamento agrícola.\n"
        "Utiliza IA generativa para análise de telemetria em tempo real\n"
        "e traduz dados orbitais em impacto para o agronegócio brasileiro.\n\n"
        "[bold]Trilha:[/bold] AgroSat — Sensoriamento Agrícola\n"
        "[bold]Satélite:[/bold] AgroSat-1 (LEO, multiespectral)\n"
        "[bold]Modelo:[/bold] gpt-oss:120b via Ollama Cloud\n"
        "[bold]Disciplina:[/bold] Prompt Engineering and AI — FIAP 2026.1",
        title="ℹ️  Sobre o Projeto",
        border_style="#06B6D4"
    ))

def run_cli(engine):
    """Loop principal da CLI."""
    show_banner()

    if not engine.is_ready():
        console.print("⚠️  Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n", style="yellow")

    while True:
        try:
            user_input = session.prompt("\n❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n👋 Encerrando Mission Control AI. Até logo!", style="#06B6D4")
            break

        if not user_input:
            continue

        if user_input == "/exit":
            console.print("\n👋 Encerrando Mission Control AI. Até logo!", style="#06B6D4")
            break

        elif user_input == "/help":
            console.print(Panel(
                "/status  → Telemetria atual do satélite\n"
                "/about   → Sobre o projeto\n"
                "/clear   → Limpar a tela\n"
                "/exit    → Encerrar o sistema\n"
                "ou digite qualquer pergunta para a ARIA analisar!",
                title="📋 Comandos disponíveis",
                border_style="#06B6D4"
            ))

        elif user_input == "/status":
            with console.status("[bold #06B6D4]Coletando telemetria do AgroSat-1...[/bold #06B6D4]"):
                snapshot = engine.status_snapshot()
            show_response(snapshot)

        elif user_input == "/about":
            show_about()

        elif user_input == "/clear":
            console.clear()
            show_banner()

        else:
            with console.status("[bold #A855F7]ARIA analisando dados da missão...[/bold #A855F7]"):
                resposta = engine.analyze(user_input)
            show_response(resposta)