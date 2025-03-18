import typer
from rich import print

app = typer.Typer(
    name="finally",
    help="Sistema de Gestão Financeira Familiar - CLI"
)

@app.command()
def info():
    """Exibe informações sobre o FinAlly"""
    print("[bold green]FinAlly[/bold green] - Sistema de Gestão Financeira Familiar")
    print("Versão: 0.1.0")

if __name__ == "__main__":
    app()
