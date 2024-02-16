#CALCULAR EL NUMERO COMUN MULTIPLO DE DOS NUMEROS
num_uno = int(input("Ingrese el primer valor: "))
num_dos = int(input("Ingrese el segundo valor: "))
if(num_uno >= num_dos):
    control = num_uno
else:
    control = num_dos
while True:
    if(control%num_uno == 0 and control%num_dos == 0):
        print("El multiplo comun multiple es",control)
        break
    control += 1        