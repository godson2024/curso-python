#IMPRIMIR FUNCIONES CON PARAMETROS
a = int(input("Ingrese el primer parametro: "))
b = int(input("Ingrese el segundo parametro: "))
def imprimirrango(a,b):
    for i in range(a,b+1):
        print(i)
imprimirrango(a,b)    