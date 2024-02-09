#IMPRIMIR LOS NUMEROS PARES DE UNA LISTA
lista_numero = []
lista_final = []
cantidad = int(input("Ingrese la cantidad "))
for i in range(cantidad):
    numero = int(input("Ingrese el valor: "))
    lista_numero.append(numero)
for i in range(cantidad):
    if(lista_numero[i]%2 == 0):
        lista_final.append(lista_numero[i])
        print(lista_numero[i], end=" ")        