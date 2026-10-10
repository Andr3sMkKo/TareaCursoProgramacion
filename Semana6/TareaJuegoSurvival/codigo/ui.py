from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress_bar import ProgressBar

console = Console()


def barra(valor, maximo=100, ancho=20):
    """Devuelve una barra de texto con el color según el valor."""
    if valor > 60:
        color = "green"
    elif valor > 30:
        color = "yellow"
    else:
        color = "red"

    # Cuántos bloques llenos y cuántos vacíos
    llenos = int(valor * ancho / maximo)
    vacios = ancho - llenos
    return f"[{color}]{'█' * llenos}[/{color}][dim]{'░' * vacios}[/dim]"


def mostrar_stats(jugador):
    """Muestra un panel con los stats del jugador."""
    tabla = Table.grid(padding=(0, 1))
    tabla.add_column(style="bold")
    tabla.add_column()

    tabla.add_row("Día",     f"[cyan]{jugador.dias}[/cyan]")
    tabla.add_row("❤️  Vida ",     f"{barra(jugador.vida)}  {jugador.vida}/100")
    tabla.add_row("⚡ Energía",   f"{barra(jugador.energia)}  {jugador.energia}/100")
    tabla.add_row("🍖 Saciedad",  f"{barra(jugador.comida)}  {jugador.comida}/100")

    console.print(Panel(tabla, title="[bold]🧍 Estado del jugador[/bold]", border_style="blue"))