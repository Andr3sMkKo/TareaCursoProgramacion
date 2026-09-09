#Calculadora de descuento

print("Calculadora de descuento")

print("¿Cual es el precio original? (Coloque solo el numero)")
preciooriginal = input()

print("¿De cuanto es el descuento? (Sin colocar el %)")
descuento = input()
if int(descuento) > 100:
    print("Estas seguro de que el descuento es mayor al 100%?")
else:
    preciofinal = float(preciooriginal) * (1-(float(descuento)/100))
    print("El precio total con el descuento es de " + str(preciofinal))

# Si el numero del preciofinal O el descuento es mas del 100
# Dar un error o volver a intentar (LISTO)