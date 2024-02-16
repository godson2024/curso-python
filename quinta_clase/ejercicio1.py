#PROMEDIO DE UNA LISTA DE NUMEROS
def promedio_lista():
    lista_numero = []
    cantidad_numero = int(input("Ingrese cantidad: "))
    for i in range(cantidad_numero):
        numero = int(input("Ingrese el numero: "))
        lista_numero.append(numero)
    suma = 0
    for i in lista_numero:
        suma += i
    promedio = suma / cantidad_numero
    return promedio
resultado = promedio_lista()
print("El promedio es:",resultado)        