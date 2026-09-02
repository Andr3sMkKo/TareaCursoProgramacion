#Numero Par o Impar

print("Numero Par o Impar")
numero = input("Escriba un numero para saber si es Par o Impar: ")

paroimpar = int(numero) % 2

if paroimpar == 0:
    print(numero + " es un numero par")
else:
    print(numero + " es un numero impar")