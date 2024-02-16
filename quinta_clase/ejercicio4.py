#CALCULAR SI UNA PALABRA ES PALINDROMO
palabra = str(input("Ingrese una palabra: "))
palabra_inv = palabra[::-1]
if(palabra == palabra_inv):
    print(palabra,"es un palindroma")
else:
    print(palabra,"no es palindroma")    