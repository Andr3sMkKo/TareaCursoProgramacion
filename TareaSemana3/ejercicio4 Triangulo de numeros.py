# Triangulo de numeros

print("Triangulo de numeros\n")
print("Creare un triangulo hecho de numeros")
num_columnas = []

while True:
    try:
        columnas = int(input("Dame el numero de columnas del triangulo: "))

        if columnas >= 51:
            terminar = input("Estas seguro de seguir? Sera demasiado grande y puede que se vea mal\n Si/No\n ==> ").capitalize()
            if terminar == "Si":
                for num in range(1,columnas+1):
                    num_columnas.append(num)
                    print(*num_columnas)
            else:
                print("Por favor, vuelve a iniciar el codigo")
                break
        elif columnas < 51:
            for num in range(1,columnas+1):
                num_columnas.append(num)
                print(*num_columnas)
            break

    except ValueError:
        print("\n!!!Hubo un error. El sistema no acepta letras o numeros menores a 1!!!\n")

# Mas de 1558 da error por maximo de digitos se puede cambiar pero es innecesario. 50 es llega a verse en la pantalla completa con mi resolucion de pantalla