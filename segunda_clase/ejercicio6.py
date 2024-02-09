#CALCULAR EL PROMEDIO DE X NUMEROS
cantidad_numero = int(input("Ingrese la cantidad de numero: "))
band = cantidad_numero
suma = 0
while(band > 0):
    numero = int(input("Ingrese el numero: "))
    suma += numero
    band -= 1
promedio = suma / cantidad_numero
print("El promedio es:",promedio)