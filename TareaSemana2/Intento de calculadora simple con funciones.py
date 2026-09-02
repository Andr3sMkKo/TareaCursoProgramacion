#1 Calculadora Simple con funciones

que_hacer = input("¿Que tipo de operacion (Suma, Resta, Multiplicacion, Division) quieres realizar? ===>  ").capitalize()
Num1, Num2 = map(int, input("Dame 2 numeros para operar (Separa los numeros por espacios) ===>  ").split())

def sum_a(Num1, Num2):
    return Num1 + Num2
def rest_a(Num1, Num2):
    return Num1 - Num2
def multiplicacio_n(Num1, Num2):
    return Num1 * Num2
def divisio_n(Num1, Num2):
    return Num1 / Num2


if que_hacer == "Suma":
    print(sum_a(Num1, Num2))
elif que_hacer == "Resta":
    print(rest_a(Num1, Num2))
elif que_hacer == "Multiplicacion":
    print(multiplicacio_n(Num1, Num2))
elif que_hacer == "Division":
    print(divisio_n(Num1, Num2))
else:
    print("Escribe algo valido como Suma, Resta, Multiplicacion, Division")