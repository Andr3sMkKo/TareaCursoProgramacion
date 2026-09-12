# Contador de vocales

print("Contador de vocales")
print("Dame una frase y contare cuantas vocales tiene\n")

frase = input()

frase_minuscula = frase.lower()
vocales = ['a','e','i','o','u']

contador = 0
for letra in frase_minuscula:
    if letra in vocales:
        contador += 1

print(f"El numero de vocales es: {contador}")


#No tuve mucho tiempo este codigo lo vi mayoritariamente con ia