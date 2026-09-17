#Calculadora de factorial

print("Calculadora de Factorial")
print("Dame un numero y te doy su factorial")

while True:
    try:
        num = int(input("==> "))

        if num < 0:
            print("Los factoriales negativos no estan definidos")
        elif num == 0:
            print("La factorial de 0 es: 1")

        factorial = 1
        for numero in range(1, num+1):
            factorial *= numero
        print(f"La factorial de {num} es: {factorial}")
        break
        
    except ValueError:
        print("Es posible que no hayas escrito un numero entero o la factorial del numero es demasiado grande")

#El maximo es 1559