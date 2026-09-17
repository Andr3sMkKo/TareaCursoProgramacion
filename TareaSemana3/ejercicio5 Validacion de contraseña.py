# Validacion de contraseña
import string

print("Validacion de contraseña")
print("Ingresa una contraseña que cumpla con los siguientes criterios:\n")

print("Tiene un minimo de 8 caracteres\nContiene al menos 1 letra mayuscula\nContiene al menos 1 letra minuscula\nContiene al menos 1 numero\nContiene al menos un caracter especial\n")

contraseña_usuario = input("Ingresa la contraseña: ")

criterios = {
    #Tiene 8 caracteres?
    "No cumple con los 8 caracteres": len(contraseña_usuario) >= 8,

    #Tiene almenos 1 mayuscula?
    "La contraseña necesita almenos 1 mayuscula": any(caracter.isupper() for caracter in contraseña_usuario),

    #Tiene almenos 1 minuscula?
    "La contraseña necesita almenos 1 minuscula": any(caracter.islower() for caracter in contraseña_usuario),

    #Tiene almenos un numero?
    "La contraseña necesita almenos 1 numero": any(caracter.isdigit() for caracter in contraseña_usuario),

    #Tiene almenos 1 caracter especial?
    "La contraseña necesita almenos 1 caracter especial": any(caracter in string.punctuation for caracter in contraseña_usuario)
}

error_falta = [error for error,condicion in criterios.items() if not condicion]

if not error_falta:
    print("Perfecto! Tu contraseña cumple con todos los criterios")
else:
    print("\nNo se cumplen estos requisitos:")
    for error in error_falta:
        print(error)