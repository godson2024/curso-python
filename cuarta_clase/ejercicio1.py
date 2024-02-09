#CALCULAR EL AREA DE UN CIRCULO CON FUNCIONES
def areacirculo():
    r = int(input("Ingrese la radio: "))
    PI = 3.1416
    area = PI*r**2
    print("El area del circulo es:",area)

areacirculo()
