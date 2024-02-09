#COMPARAR NUMEROS MAYORES
numero_uno = int(input("Ingresar el primer numero"))
numero_dos = int(input("Ingresar el segundo numero"))

if (numero_uno > numero_dos):
    print(numero_uno," es mayor que ",numero_dos)
elif (numero_uno == numero_dos):
    print(numero_uno," es igual a ",numero_dos)
else:
    print(numero_uno," es menor que ",numero_dos)
while(numero_uno > numero_dos):
    print(numero_uno," es mucho mayor que ",numero_dos)
    numero_dos += 1
    
            
    
