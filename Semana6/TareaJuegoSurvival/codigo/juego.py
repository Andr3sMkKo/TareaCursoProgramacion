from pathlib import Path
import pandas as pd
from rich.console import Console
from pyfiglet import figlet_format

from jugador import Jugador
from menu import jugar

console = Console()

# ─── 1. Cargar el Excel ───
RUTA_RAIZ = Path(__file__).parent.parent
RUTA_EXCEL = RUTA_RAIZ / "eventos" / "eventos.xlsx"

df_eventos = pd.read_excel(RUTA_EXCEL, sheet_name="eventos")
df_efectos = pd.read_excel(RUTA_EXCEL, sheet_name="efectos")
df_finales = pd.read_excel(RUTA_EXCEL, sheet_name="finales")
df_config  = pd.read_excel(RUTA_EXCEL, sheet_name="config")

# ─── 2. Convertir a diccionarios ───
eventos = {}
for _, fila in df_eventos.iterrows():
    opciones = []
    for i in range(1, 4):
        valor = fila[f"opcion_{i}"]
        if pd.notna(valor):
            opciones.append(valor)
    eventos[int(fila["id"])] = {
        "nombre_evento": fila["nombre_evento"],
        "zona": fila["zona"],
        "texto": fila["texto"],
        "opciones": opciones
    }

efectos = {}
for _, fila in df_efectos.iterrows():
    clave = (int(fila["evento_id"]), int(fila["opcion"]))
    efectos[clave] = {
        "vida": int(fila["vida"]),
        "energia": int(fila["energia"]),
        "comida": int(fila["comida"]),
        "siguiente": int(fila["siguiente"])
    }

finales = {}
for _, fila in df_finales.iterrows():
    finales[int(fila["id"])] = {
        "final": fila["final"],
        "condicion": fila["condicion"]
    }

config = dict(zip(df_config["clave"], df_config.iloc[:, 1]))

# ─── 3. Mostrar título ───
console.print(f"[bold red]{figlet_format(config['titulo'], font="smslant")}[/bold red]")

# ─── 4. Crear jugador ───
jugador = Jugador(
    nombre="Náufrago",
    vida=config["vida_inicial"],
    energia=config["energia_inicial"],
    comida=config["comida_inicial"]
)

console.print(f"[green]Bienvenido, {jugador.nombre}.[/green]")
console.print("[dim]Presiona Ctrl+C en cualquier momento para salir.[/dim]\n")

# ─── 5. ¡Jugar! ───
jugar(jugador, eventos, efectos, finales, evento_inicial=config["evento_inicial"])