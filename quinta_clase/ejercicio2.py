#VERIFICAR SI UN NUMERO ES PRIMO
valor = int(input("Ingrese el numero: "))
lista_numero = []
cont=0
for i in range(2,valor):
    if(valor%i == 0):
        cont = 1
if(cont == 0):
    print("El numero",valor," es primo")   
else:
    print("El numero",valor,"no es primo")