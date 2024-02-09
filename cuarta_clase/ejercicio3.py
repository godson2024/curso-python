#HACER UNA FUNCION QUE CALCULE EL FACTORIAL DE UN NUMEROQUE LE PASE A TRAVES DE UN PARAMETRO
numero = int(input("Ingrese el valor: "))
def factorial(numero):
    suma = 1
    while(numero >= 2):
        suma *= numero
        numero -= 1
    print(suma)
factorial(numero)        