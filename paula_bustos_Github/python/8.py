#Hacer que cuando ingrese los numeros los pase a binario
user = int(input("Ingrese numero binario: "))
temp = "{0:b}".format(user)

print(temp)