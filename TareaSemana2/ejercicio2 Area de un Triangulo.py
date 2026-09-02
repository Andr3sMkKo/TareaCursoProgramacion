#2 Area de un Triangulo
# área = (base * altura) / 2

print("Area de un Triangulo")

print("¿Cual es la base del triangulo? ")
base = input()
print("¿Cual es la altura del triangulo?")
altura = input()
area = (int(base) * int(altura)) / 2

print("El area del triangulo es " + str(area))

#Encontrar una forma de leer o diferenciar si el input es un numero o letra 
print("Area de un Triangulo #2")

while True:
    try:
        print("¿Cual es la base del triangulo? ")
        base = int(input())
        print("¿Cual es la altura del triangulo?")
        altura = int(input())
        area = (base * altura) / 2
        print("El area del triangulo es " + str(area))
        break
    except ValueError:
        print("Por favor ingresa numeros")