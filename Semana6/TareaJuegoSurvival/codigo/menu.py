from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from ui import mostrar_stats

console = Console()

def mostrar_final(final, jugador, tipo="normal"):
    """Muestra un panel con el final del juego."""
    color = {
        "bueno":   "green",
        "malo":    "red",
        "neutral": "yellow"
    }.get(tipo, "cyan")

    # Reemplazamos {dias} por el valor real del jugador
    texto = final["final"].replace("{dias}", str(jugador.dias))

    console.print()
    console.print(Panel(
        f"[bold]{texto}[/bold]\n\n"
        f"[dim]Sobreviviste {jugador.dias} día(s).[/dim]",
        title="🏁 FIN DEL JUEGO",
        border_style=color
    ))
    console.print()


def buscar_final(finales, condicion):
    """Busca en el diccionario finales uno que coincida con la condición."""
    for fid, datos in finales.items():
        if datos["condicion"] == condicion:
            return fid, datos
    return None, None


def buscar_tipo_final(condicion):
    """Determina el color del final según su condición."""
    if "escapar" in condicion or "ganar" in condicion:
        return "bueno"
    if "vida_0" in condicion or "comida_0" in condicion:
        return "malo"
    return "neutral"


def mostrar_evento(evento):
    texto = f"[bold]{evento['texto']}[/bold]"
    console.print(Panel(texto, title=f"🌴 {evento['zona']}", border_style="cyan"))


def mostrar_opciones(opciones):
    console.print("\n[bold yellow]¿Qué haces?[/bold yellow]")
    for i, opcion in enumerate(opciones, start=1):
        console.print(f"  [bold cyan]{i}.[/bold cyan] {opcion}")
    console.print()


def pedir_opcion(cantidad):
    while True:
        eleccion = Prompt.ask("[bold green]Elige una opción[/bold green]")
        if eleccion.isdigit():
            numero = int(eleccion)
            if 1 <= numero <= cantidad:
                return numero
        console.print(f"[red]Opción inválida. Debe ser un número entre 1 y {cantidad}.[/red]")


def jugar(jugador, eventos, efectos, finales, evento_inicial=1):
    evento_actual = evento_inicial

    while jugador.vivo:
        # mostrar stats 
        console.print()
        mostrar_stats(jugador)
        console.print()

        # Mostrar el evento actual 
        if evento_actual not in eventos:
            console.print(f"[red]Error: el evento {evento_actual} no existe.[/red]")
            break

        evento = eventos[evento_actual]
        mostrar_evento(evento)

        # Mostrar las opciones
        opciones = evento["opciones"]
        mostrar_opciones(opciones)

        # Pedir al jugador
        eleccion = pedir_opcion(len(opciones))

        # Aplicar el efecto
        clave = (evento_actual, eleccion)
        if clave not in efectos:
            console.print(f"[red]Error: no hay efecto para evento {evento_actual}, opción {eleccion}.[/red]")
            break

        efecto = efectos[clave]
        jugador.aplicar_efecto(
            vida=efecto["vida"],
            energia=efecto["energia"],
            comida=efecto["comida"]
        )

        # Avisar si se desmayo 
        if jugador.durmiendo:
            console.print(f"\n[italic yellow]Te desmayas por agotamiento...[/italic yellow]")
            console.print(f"[bold yellow]Amanece el día {jugador.dias}.[/bold yellow]")
            console.print(f"[dim]Recuperas algo de energía, pero el comida aprieta.[/dim]\n")
            jugador.durmiendo = False


        # Verificar si sigue vivo
        if not jugador.vivo:
            # Determinar por qué murió
            if jugador.vida <= 0:
                condicion = "vida_0"
            elif jugador.comida <= 0:
                condicion = "comida_0"
            else:
                condicion = "vida_0"  # por defecto

            fid, final = buscar_final(finales, condicion)
            if final:
                mostrar_final(final, jugador, tipo="malo")
            else:
                console.print("[bold red]💀 Has muerto.[/bold red]")
            break

        # Siguiente evento
        siguiente = efecto["siguiente"]

        # final
        if siguiente in finales:
            final = finales[siguiente]
            tipo = buscar_tipo_final(final["condicion"])
            mostrar_final(final, jugador, tipo=tipo)
            break

        # aun no esta hecho
        if siguiente == -1:
            console.print("[yellow]Fin del camino actual (aún por implementar).[/yellow]")
            break

        # siguiente evento
        evento_actual = siguiente

    return jugador