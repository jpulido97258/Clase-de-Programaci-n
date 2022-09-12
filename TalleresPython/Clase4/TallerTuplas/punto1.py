#Aqui definimos la tupla:

tuplaA = ("Taller","Algoritmos","Programación",[2,9,2022]);
tallerEnTupla = False; #Esto es para verificar si algo esta en la tupla
print("Los primeros 3 valores de la tupla son: " , tuplaA[:3]);

# el bucle for revisa todas las posiciones y verificar si la palabra "taller" esta en la tupla.
for i in tuplaA:
    if i == "Taller":
        tallerEnTupla = True
print("¿Taller esta en la tupla?: " , tallerEnTupla);

#en esta parte imprimimos la posicion de la palabra "programación" en la tupla
posicion = 0

for j in tuplaA:
    if j == "Programación":
        print("Programacion se encuentra en la posicion: " , posicion);
        break
    posicion = posicion+1;

#Aqui imprimimos la longitud de la tupla.

Longitud = len(tuplaA)
print("La cantidad de elementos en la tupla es de: " , Longitud)

# Aqui hacemos la lista a partir de la tupla. (Y la mostramos en pantalla)

Lista = [];
posicionLista = 0;

for k in tuplaA:
    Lista.append(tuplaA[posicionLista])
    posicionLista = posicionLista + 1;
print("La lista creada a partir de la tupla es: " , Lista)
    

