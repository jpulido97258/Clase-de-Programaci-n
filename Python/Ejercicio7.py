num1 = input('Ingresa un número ')
num2 = input('Ingresa otro número ')
resultado1 = num1%2
resultado2 = num2%3
print ('El resultado inicial es: ' , resultado1)
print ('El resultado secundario es: ' , resultado2)


if resultado1 != resultado2:    
    input('Vuelve a ingresar un numero')
else:
    print('Ha terminado el ejercicio')
