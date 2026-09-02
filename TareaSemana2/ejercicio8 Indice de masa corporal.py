# Indice de masa corporal (IMC)
# (IMC = peso (kg)/ [estatura (m)]2

print("Cual es tu Indice de masa corporal (IMC)")

print("¿Cual es tu estatura en metros?")
estatura = input()

print("¿Cual es tu peso en kilogramos?")
peso = input()

print(float(peso) / (float(estatura) ** 2))