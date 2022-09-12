# Aqui creamos una tupla a partir de lo que ingresa el usuario separado por espacios

listaB = input().split(" "); # esto crea una lista
tuplaB = tuple(listaB) # aqui transformamos la lista en tupla
print(tuplaB)

#Imprimimos las posiciones impares de la tupla:

for i in range(0,len(tuplaB)):
    if i%2 != 0:
        print("En la posicion" , i , "esta el valor: " , tuplaB[i]);


#tupla a lista, valor de lista a entero

sumaTupla = 0;

for i in range(0,len(tuplaB)):
    sumaTupla = sumaTupla + int(tuplaB[i])
print("La suma de los valores de la tupla es: ", sumaTupla)

tuplaB = min(tuplaB)
print("El valor mas pequeño de la tupla es: ", tuplaB)
    
