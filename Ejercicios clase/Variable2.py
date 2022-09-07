#Ejercicio hallar el area de un trapecio

h = input("Digitar altura del trapecio:")
b = input("Digitar base menor del trapecio:")
B = input("Digitar base mayor del trapecio:")

list = ('Altura del trapecio:',h, 'Base menor:',b, 'Base mayor:',B)

print(list)

res = (int(h)*int(b)*int(B)/(2))

print ("El area del trapecio es igual a:", res)
