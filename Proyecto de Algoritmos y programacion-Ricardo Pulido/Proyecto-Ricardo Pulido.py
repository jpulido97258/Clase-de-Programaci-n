def introducirNumeros ():
    global numero1, numero2
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))

def sumar (a, b):
    print("La suma de ",a," + ",b," = ",a+b)

def restar (a, b):
    print("La resta de ",a," - ",b," = ",a-b)

def multiplicación (a, b):
    print("La multiplicación de ",a," x ",b," = ",a*b)

def division (a, b):
    if b == 0:
        print("No se puede dividir entre cero")
    else: 
        print ("La división de ",a," / ",b," = ",a/b)

while True:
    print("""
    Hola, como estas? Soy tu calculadora personal
    Indique la operación a realizar:

    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir de la calculadora
    """)

    eleccion = int (input ())


    if eleccion == 1:
        introducirNumeros()
        sumar(numero1, numero2)
    elif eleccion == 2:
        introducirNumeros()
        restar(numero1, numero2)
    elif eleccion == 3:
        introducirNumeros()
        multiplicación(numero1, numero2)
    elif eleccion == 4:
        introducirNumeros()
        division(numero1, numero2)
    elif eleccion == 5:
        print("Hasta pronto")
        break