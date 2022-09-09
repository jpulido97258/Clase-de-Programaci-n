# otros tipos de comandos con for 
from ast import Str
from smtpd import MailmanProxy
from typing import Iterable
from unicodedata import numeric


nums = [1,3,5,6,7]
for n in nums:
    if n == 7:
        break
    print(n)

# este codigo te dira si es verdadero
coleccion = [2,4,5,7,8,9,3,4]

for e in coleccion: 
    if e % 2!= 0:
        continue
    print(e)
# este codigo es para separar los numeros 
numeros =  [6,4,5,7,6,9,79,45,15]
for n in numeros: 
    if n == 3: 
        break
else: 
    print ("No se encontro el numero 3")
# nuevo proyecto usuario 

unlogin= Str(input("colocar su usario") ) 
C = ("Nico")

for n in unlogin:
    if unlogin == C:
        break
else:
    print ("El usuario es Incorrecto")

Contraseña= Str(input("colocar su usario") ) 
D = "nico123"

for n in Contraseña:
    if unlogin == D:
        break
else:
    print ("El contraseña es Incorrecta")
    
        







