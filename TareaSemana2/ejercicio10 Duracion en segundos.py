# Duracion en segundos

print("Conversion de tiempo a segundos")

print("¿Que duracion en horas, minutos y segundos quieres convertir a segundos?")
horas = input("Cuantas horas: ")
minutos = input("Cuantos minutos: ")
segundos= input("Cuantos segundos: ")

conversion = (int(horas) * 3600) + (int(minutos) * 60) + int(segundos)
print("En total son " + str(conversion) + " segundos")