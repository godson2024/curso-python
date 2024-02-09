#REVISAR SI EL NOMBRE DE UNA PERSONA TIENE MAS DE 5 CARACTERES
nombre = str(input("Ingrese el nombre de la persona: "))
cantidad = len(nombre)
if (len(nombre) > 5):
    print(nombre,"tiene",cantidad,"caracteres")
else:
    print(nombre,"tiene menos caracteres",cantidad)  