#IR DE LETRA EN LETRA DE UN TEXTO PARA SABER CANTIDADES DE VOCALES TIENE
texto = str(input("Ingrese un el texto: "))
vocal = 0
for valor in texto:
    if(valor == 'a' or valor == 'e' or valor == 'i' or valor == 'o' or valor == 'u' ):
        vocal += 1
print("La cantidad de vocal es:",vocal) 