#1 Calculadora Simple
oraciones = {
    "inicio" : "Calculator: Que operacion simple quieres realizar? (Suma, Resta, Multiplicacion, Division)",
    "pedir" : "Dame 2 numeros separados por un espacio que desees",
    "operaciones" : [" sumar: ", " restar: ", " multiplicar: ", " dividir: "]}

print(oraciones["inicio"])
calc = input("=>  ").capitalize()

if calc == "Suma":
    numsuma = input(oraciones["pedir"] + oraciones["operaciones"][0]).split()
    sum1 = int(numsuma[0])
    sum2 = int(numsuma[1])
    suma = sum1 + sum2
    print("El resultado es: " + str(suma))

elif calc == "Resta":
    numresta = input(oraciones["pedir"] + oraciones["operaciones"][1]).split()
    subst1 = int(numresta[0])
    subst2 = int(numresta[1])
    resta = subst1 - subst2
    print("El resultado es: " + str(resta))

elif calc == "Multiplicacion":
    nummulti = input(oraciones["pedir"] + oraciones["operaciones"][2]).split()
    mult1 = int(nummulti[0])
    mult2 = int(nummulti[1])
    multiplicacion = mult1 * mult2
    print("El resultado es:" + str(multiplicacion))

elif calc == "Division":
    numdivi = input(oraciones["pedir"] + oraciones["operaciones"][3]).split()
    div1 = int(numdivi[0])
    div2 = int(numdivi[1])
    division = div1 / div2
    print("El resultado es: " + str(division))

else:
    print("No puedo hacer lo que me pides. Escribe Suma, Resta, Multiplicacion o Division")