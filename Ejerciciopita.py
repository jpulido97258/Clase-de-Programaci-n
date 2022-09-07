# Vamos a calcular el promedio de notas de este corte
print("Las notas del corte")
Integral = print("Colocar las notas que ha sacado en el corte de Integral  que no sean mas de 5") # ingresar las notas 
a = float (input("coloque la primera nota"))
b = float (input("coloque la segunda nota"))
c = float (input("coloque la tercera nota"))
d= float (input("coloque la cuarta nota"))
resin = float (a+b+c+d / 4 )
print("el resultado es:", resin)


Programacion = print("Colocar las notas que ha sacado en el corte de Programacion que no sean mas de 5") # ingresar las notas 
a = float (input("coloque la primera nota"))
b = float (input("coloque la segunda nota"))
c = float (input("coloque la tercera nota"))
d= float (input("coloque la cuarta nota"))
resin2 = float (a+b+c+d / 4 )
print("el resultado es:", resin2)

Constitucion = print("Colocar las notas que ha sacado en el corte  de Constitucion que no sean mas de 5") # ingresar las notas 
a = float (input("coloque la primera nota"))
b = float (input("coloque la segunda nota"))
c = float (input("coloque la tercera nota"))
d= float (input("coloque la cuarta nota"))
resin3 = float (a+b+c+d / 4 ) 
print("el resultado es:", resin3)
Fisica = print("Colocar las notas que ha sacado en el corte de Fisica que no sean mas de 5") # ingresar las notas 
a = float (input("coloque la primera nota"))
b = float (input("coloque la segunda nota"))
c = float (input("coloque la tercera nota"))
d= float (input("coloque la cuarta nota"))
resin4 = float (a+b+c+d / 4 )
print("el resultado es:", resin4)


print("Cual de las clases va mejor segun las otras")

if resin > resin2:
    print ("vas mejor en integral")
elif resin < resin2:
    print ("vas mejor en programacion")
   


#booleano
condicion1 = resin != resin2 
print (condicion1)
