from audioop import reverse
import random
suma1 = 0
suma2 = 0 
suma3 = 0 
suma4 = 0
suma5 = 0
suma6 = 0
suma7 = 0

print('=========================================================================================')
print('Bienvenido al juego de dadito')
print('Las reglas son simples, lanza el dado para acomular puntos')
print('Puedes lanzarlo cuantas veces quieras, pero si sacas 1 se te quitaran todos los puntos')
print('Para ello, puedes dejar de lanzar el dado y asi obtener todos los puntos')
print('Quien llegue a la cantidad de puntos deseada ganará el juego')
print('==========================================================================================')
print('JUGUEMOS!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma1 = suma1+dado
    else:
        break
    if(dado == 1):
        break
if(suma1>0) and (lanzar == 'b'):
    print('Haz ganado ', suma1, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma2 = suma2+dado
    else:
        break
    if(dado == 1):
        break
if(suma2>0) and (lanzar == 'b'):
    print('Haz ganado ', suma2, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma3 = suma3+dado
    else:
        break
    if(dado == 1):
        break
if(suma3>0) and (lanzar == 'b'):
    print('Haz ganado ', suma3, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma4 = suma4+dado
    else:
        break
    if(dado == 1):
        break
if(suma4>0) and (lanzar == 'b'):
    print('Haz ganado ', suma4, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma5 = suma5+dado
    else:
        break
    if(dado == 1):
        break
if(suma5>0) and (lanzar == 'b'):
    print('Haz ganado ', suma5, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma6 = suma6+dado
    else:
        break
    if(dado == 1):
        break
if(suma6>0) and (lanzar == 'b'):
    print('Haz ganado ', suma6, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

while True:
    lanzar = (input('Para lanzar el dado presiona (a), para asegurar presiona (b) '))
    if(lanzar != 'b'):
        dado = random.randint(1, 6)
        print('El numero que salió fue: ', dado)
        suma7 = suma7+dado
    else:
        break
    if(dado == 1):
        break
if(suma7>0) and (lanzar == 'b'):
    print('Haz ganado ', suma7, 'puntos en total!!!')    
else:
    print('Haz perdido los puntos acomulados!!!')

tot = suma1 + suma2 + suma3 + suma4 + suma5 + suma6 + suma7
print('Haz conseguido un total de', tot, 'puntos!!')

if (tot >= 40):
    print('Felicidades!!!!')
    print('HAZ GANADO EL JUEGO :D' )
else:
    print('No haz conseguido la cantidad de puntos necesaria :(')
    print('Suerte para el proximo juego')

