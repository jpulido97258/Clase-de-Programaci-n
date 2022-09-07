#Hacer que el usuario ingrese dos numeros y nos diga que operacion quiere hacer
num1 = float(input("Digite su primer numero"))
num2 = float(input("Digite su segundo numero"))
operacion = input("¿Simbolo de la operacion?")

if operacion == "suma" or operacion == "+":
    print("El resultado es:", num1+num2)
elif operacion == "resta" or operacion == "-":
    print("El resultado es:", num1-num2)
elif operacion == "multiplicacion" or operacion == "*":
    print("El resultado es:", num1*num2)
elif operacion == "division" or operacion == "/":
    if num2 != 0:
        print("El resultado es:", num1/num2)
    else:
        print("Division por 0 no es posible")