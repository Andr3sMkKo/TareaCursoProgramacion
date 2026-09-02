#Mayor de dos numeros

print("¿Que numero es mayor?")
print("Escribe 2 numeros que quieras determinar cual es mayor (Separa los numeros con un espacio) ")
num1, num2 = input().split()

if float(num1) > float(num2):
    print(num1 + " es mayor que " + num2)
elif float(num2) > float(num1):
    print(num2 + " es mayor que " + num1)

#Este codigo no acepta fracciones ejm: 9/5