# Lista de dinosaurios (usando tuplas)

# Crear una lista de dinosaurios, hacer un tipo de diccionario de dinosaurios con tuplas
# Pedir al usuario el nombre de un dinosaurio
# Darle los datos del dinosaurio que ingreso el usuario

#Los datos iran en este orden:
# ("Nombre", "Especie", "Dieta", "Periodo")

datos_dino = [("Tiranosaurio","Tiranosaurus Rex", "Carnivoro", "Cretacico Tardio"),
            ("Velociraptor", "Mongoliensis/Osmolskae", "Carnivoro", "Cretacico Superior/Campanienese"),
            ("Triceratops", "Horridus/Prorsus", "Herviboro", "Cretacico Superior"),
            ("Estegosaurio", "Stenops/Armatus/Ungulatus/Sulcatus", "Herviboro", "Jurasico Tardio/Superior"),
            ("Braquiosaurio", "Brachiosaurus Altithorax", "Herviboro", "Jurasico Superior"),
            ("Spinosaurio", "Spinosaurus Aegyptiacus", "Carnivoro", "Cretacico Superior"),]
nombres_dino = ["Tiranosaurio", "Velociraptor", "Triceratops", "Estegosaurio", "Braquiosaurio", "Spinosaurio"]

def info_dino(datos_dino, nombre_dino):
    for dino in datos_dino:
        if nombre_dino in dino:
            print("\nDatos: Nombre => Especie => Dieta => Periodo")
            print(f"{dino}\n")
            return
    
    print("El dinosaurio no esta en la base de datos")
    return

print("Base de datos de Dinosaurios (Dicciosaurio)")
print("\nActualmente los dinosaurios disponibles son:\nTiranosaurio, Velociraptor, Triceratops, Estegosaurio, Braquiosaurio, Spinosaurio\n")

while True:
    try:
        opcion = int(input("1.Ingresar dinosaurio y ver datos\n2.Que dinosaurios tiene la base de datos\n3.Salir\n==> "))
        if opcion == 1:
            que_dino = input("Ingresa el nombre del dinosaurio:\n\n").title()
            info_dino(datos_dino, que_dino)
            #info_dino()

        elif opcion == 2:
            
            print("\nActualmente en la base de datos tenemos:")
            print(*nombres_dino, sep=" | ")
            print("")
            #cuantos_dino()

        elif opcion == 3:
            print("Nos vemos luego!")
            break

        else:
            raise ValueError("\nOpcion no valida\n")
            
    except ValueError:
        print("\nOpcion no valida\n")