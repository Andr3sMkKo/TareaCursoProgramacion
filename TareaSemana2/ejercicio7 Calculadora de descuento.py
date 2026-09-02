#Calculadora de descuento

print("Calculadora de descuento")

print("¿Cual es el precio original? (Coloque solo el numero)")
preciooriginal = input()

print("¿De cuanto es el descuento? (Sin colocar el %)")
descuento = input()

preciofinal = float(preciooriginal) * (1-(float(descuento)/100))
print("El precio descontado es de " + str(preciofinal))