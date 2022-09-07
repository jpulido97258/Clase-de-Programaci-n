num1=float(input('inserta el primer número ')) #define la varible y le pide al usuario los valores
num2=float(input('inserta el segundo número '))
resultado1=num1%2 #realiza la operacion mencionada
resultado2=num2%3
print ('el resultado inicial es ',resultado1) #le muestra al usuario el resultado de la operación hecha
print ('el resultado secundario es ', resultado2)


if resultado1!=resultado2: #nos condiciona para poder saber si debemos pedirle otro número al usuario o no
    input('el resultado dio valores diferentes, vuelve a ingresar un número')
else:
    print('el resultado dió los mismos valores, ha terminado el ejercicio')