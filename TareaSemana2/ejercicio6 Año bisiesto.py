#Año bisiesto

print("Determinador de año bisiesto")
print("Escriba un año:")
año = input()

if (int(año)%4 == 0 and int(año)%100 != 0) or (int(año)%400 == 0):
    print(año + " es un año bisiesto")
else:
    print(año + " no es un año bisiesto")