import pandas as pd
from pathlib import Path

# ubicacion del excel
ruta_carpeta_corazon = Path(__file__).parent.parent
ruta_excel = ruta_carpeta_corazon / "eventos" / "eventos.xlsx"
# debug
# print(f"ruta del excel: {ruta_excel}")
# print(f"{ruta_excel.exists()}")

df_eventos = pd.read_excel(ruta_excel, sheet_name="eventos")
df_efectos = pd.read_excel(ruta_excel, sheet_name="efectos")
df_finales = pd.read_excel(ruta_excel, sheet_name="finales")
df_config = pd.read_excel(ruta_excel, sheet_name="config")

# debug
"""
print("\n---------------------------")
print(df_eventos)
print("\n---------------------------")
print(df_efectos)
print("\n---------------------------")
print(df_finales)
print("\n---------------------------")
print(df_config)
"""

eventos = {}
for indice, fila in df_eventos.iterrows():
    opciones = []
    for n in range(1,4):
        valor = fila[f"opcion_{n}"]
        if pd.notna(valor):
            opciones.append(valor)
    eventos[int(fila["id"])] = {
        "nombre_evento" : fila["nombre_evento"],
        "zona" : fila["zona"],
        "texto" : fila["texto"],
        "opciones" : opciones
    }
efectos = {}
for indice, fila in df_efectos.iterrows():
    clave = (int(fila["evento_id"]), int(fila["opcion"]))
    efectos[clave] = {
        "vida": int(fila["vida"]),
        "energia": int(fila["energia"]),
        "comida": int(fila["comida"]),
        "siguiente": int(fila["siguiente"])
    }
finales = {}
for indice, fila in df_finales.iterrows():
    finales[int(fila["id"])] = {
        "final" : fila["final"],
        "condicion" : fila["condicion"]
    }
config = {}
for indice, fila in df_config.iterrows():
    config[fila["clave"]] = int(fila["valor"])

#debug
"""
print("\n=== EVENTOS CONVERTIDOS A DICCIONARIO ===")
print(f"Total de eventos: {len(eventos)}")
print(f"Ejemplo evento 1: {eventos[1]}")
print(f"Ejemplo evento 8: {eventos[8]}")
print("\n=== EFECTOS CONVERTIDOS A DICCIONARIO ===")
print(f"Total de efectos: {len(efectos)}")
print(f"Ejemplo efecto (1,1): {efectos[(1, 1)]}")
print("\n=== FINALES CONVERTIDOS A DICCIONARIO ===")
print(finales)
print("\n=== CONFIG CONVERTIDA A DICCIONARIO ===")
print(config)
"""