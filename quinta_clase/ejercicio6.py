#DSISTEMA DE REGISTRO DE PASAJEROS
pasajeros = {}
def menu():
    global pasajeros
    opcion = int(input("""Seleccione la opcion
    [1]REGISTRAR PASAJERO
    [2]LISTAR PASAJERO
    [3]BORRAR PASAJERO
    [4]SALIR                                 
    """))

    if opcion == 1:
        nombre = str(input("el nombre: "))
        cedula = int(input("la cedula: "))
        asiento = str(input("El asiento: "))
        pasajeros[asiento] = [nombre,cedula]

    if opcion == 2:
        for llave,valor in pasajeros.items():
            print("El asiento:",llave,"le corresponde a:",valor[0])

    if opcion == 3:
        pasajeros = {}

    if opcion == 4:
        quit()

    menu()        

menu()