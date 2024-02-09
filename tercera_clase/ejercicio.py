#GENERAR EL PROMEDIO DE UNA LISTA DE CALIFICACIONES DE UN ALUMNO
lista_nota = []
cantidad = int(input("Ingrese la cantidad "))
total = 0
for i in range(cantidad):
    nota = int(input("Ingrese la nota: "))
    lista_nota.append(nota)
    total += nota
promedio = total / cantidad 
print("El promedio es: ",promedio)   