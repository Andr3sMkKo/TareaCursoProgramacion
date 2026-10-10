from jugador import Jugador

j = Jugador(nombre="Náufrago", vida=100, energia=100, comida=100)
print("=== Inicio ===")
print(j)

print("\n=== Gasta energía y come ===")
j.aplicar_efecto(energia=-30, comida=20)  # come algo, no puede pasar de 100
print(j)

print("\n=== Se agota la energía (se desmaya) ===")
j.aplicar_efecto(energia=-100)
print(j)
print(f"¿Dormido? {j.durmiendo}")

print("\n=== Eventualmente muere de inanición ===")
j.aplicar_efecto(comida=-100)
print(j)
print(f"¿Vivo? {j.vivo}")