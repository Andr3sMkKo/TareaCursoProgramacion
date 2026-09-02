#Conversion de temperatura
#Celsius ==> Fahrenheit (°F = (°C × 1.8) + 32)
#Celsius ==> Kelvin (K = °C + 273.15)

print("Conversor de Temperaturas (Celsius, Fahrenheit, Kelvin)")

temperaturas = ["Celsius", "Fahrenheit", "Kelvin"]
print("Elige 2 temperaturas que quieras convertir en este orden A ==> B")
temp1 = input("Temperatura que quieres convertir: ").capitalize()
temp2 = input("Temperatura resultante: ").capitalize()

if (temp1 or temp2) not in temperaturas :
    print("Error: Probablemente hayas escrito algo mal")
else:
    print("Separando por un espacio coloca ambos grados de las temperaturas en el mismo orden (A ==> B)")
    grados1 = input()

    #grados1 para cada conversion sera siempre la palabra clave del dict
    #grados1 en celsius es celsius y misma logica para fahrenheit y kelvin
    conversiones = {"celsius" : [(int(grados1) * 9/5) + 32, int(grados1) + 273.15 ],
                    "fahrenheit" : [(int(grados1) - 32) * 5/9, (int(grados1) - 32) * 5/9 + 273.15],
                    "kelvin" : [int(grados1) - 273.15, (int(grados1)- 273.15) * 9/5 + 32]
                    }
    
    if temp1 == "Celsius":
        if temp2 == "Fahrenheit":
            print(conversiones["celsius"][0])
        elif temp2 == "Kelvin":
            print(conversiones["celsius"][1])

    elif temp1 == "Fahrenheit":
        if temp2 == "Celsius":
            print(conversiones["fahrenheit"][0])
        elif temp2 == "Kelvin":
            print(conversiones["fahrenheit"][1])

    elif temp1 == "Kelvin":
        if temp2 == "Celsius":
            print(conversiones["kelvin"][0])
        elif temp2 == "Fahrenheit":
            print(conversiones["kelvin"][1])


# Como colocar este error en caso de que grados1 no sea un numero
    #else: 
        #print("Error: Probablemente no hayas puesto numeros o espaciado de forma correcta")