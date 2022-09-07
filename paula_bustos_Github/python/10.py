num1 = float(input("Digite su primer numero"))
num2 = float(input("Digite su segundo numero"))
resultado1 = num1%2
resultado2 = num2%3
print("El resultado inicial es: ", resultado1)
print("El resultado secundario es: ", resultado2)
#booleano
condicion1 = resultado1 != resultado2
print(condicion1)
if condicion1 == True:
    print("Los numeros son diferentes")
else:
    print("Los numeros son iguales")