#COMPARAR EL MAYOR DE VARIOS NUMEROS
numeros = []

# Le agregamos 3 números
for i in range(1,10):
  numeros.append(i)

# Asumir que el mayor es el primero de la lista
mayor = numeros[0]
# Recorrer y comparar
for i in numeros:
    if i > mayor:
        mayor = i
# Imprimir el resultado
print("Mayor:", mayor)