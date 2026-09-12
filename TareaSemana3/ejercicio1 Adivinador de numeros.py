# Adivinador de numeros
# Generar un numero aleatorio y hacer que el usuario adivine el numero (Darle pistas)

print("Juego de Adivinar el Numero")

import random
numero_random = random.randint(0,20)
print("Elige un numero entre el 0 y el 20")
numero_elegido = int

while str(numero_elegido) != str(numero_random):
    try: 
        numero_elegido = input("==> ")
        if int(numero_elegido) == int(numero_random):
            print(f"Correcto! El numero era {numero_random}")
            break
        
        elif int(numero_elegido) > int(numero_random):
            print(f"El numero {numero_elegido} es incorrecto. Intenta uno mas pequeño")
            continue

        elif int(numero_elegido) < int(numero_random):
            print(f"El numero {numero_elegido} es incorrecto. Intenta uno mas grande")
            continue

    except ValueError:
        print("No colocaste un numero? Vuelve a intentarlo")