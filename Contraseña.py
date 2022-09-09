from ast import While


contras = 1430
cont = 1
dig = float (input('Ingrese la contraseña de 4 digitos '))
while contras != dig:
    dig = float (input('Contraseña incorrecta, Ingrese la contraseña de 4 digitos '))
    cont = cont + 1
print ('Contraseña correcta')




