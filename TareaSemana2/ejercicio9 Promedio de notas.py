# Promedio de notas

print("Promedio de notas")

print("Indique 3 notas separadas por un espacio para saber el promedio:")
nota1, nota2, nota3 = input().split()

promedio = (int(nota1) + int(nota2) + int(nota3))/3
print("El promedio es " + str(promedio))