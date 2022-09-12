#PRIMER PUNTO

A=("Taller","algoritmos","programacion",[2,9,2022])
print(A[0:3])

if "Taller" in A:
    print ("Taller si esta en la tupla")

print ("Su posicion es:")
print (A.index("programacion"))

print ("Su longitud es:")
print (len(A))

print (A)