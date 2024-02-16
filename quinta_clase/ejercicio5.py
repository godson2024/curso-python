#FACTORIAL CON 
n = int(input("Ingrese un valor: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

resultado = factorial(n)
print(resultado)