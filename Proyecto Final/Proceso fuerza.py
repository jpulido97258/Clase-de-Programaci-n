print('Vamos a medir que tal estan tus niveles de deztraza fisica')
print('Vas a medir la fuerza de tus brazos, piernas, abdomen yesaplda, ademas de velocidad y Hagilidad')
print('Vamos hacer un test rapido para cada parte muscular')
print('Vas a seguir las siguintes instrucciones: ')
print('Colocate frente a una pared y haz voleo y cuantas repeticiones puedes hacer seguidas')
esta1=int(input('¿Cuantas lograste hacer? '))
print('Ahora vas a realizar sentadillas con salto a hacer el maximo de repeticiones, deben ser sin descanso')
esta2=int(input('¿Cuantas lograste hacer? '))
print('Ahoras vas a realizar el numero maximo de saltos de bloqueo que puedas, estos saltos deben ser segudidos')
esta3=int(input('¿Cuantas lograste hacer? '))
print('Vas a realizar el numero maximo de repeticiones de flexiones de pecho, debes bajarr hasta rozar el pecho con el suelo yt subir hasta extender casi completamente los codos')
esta4=int(input('¿Cuantas lograste hacer? '))
print('Ahora vas a hacert dorsales, haz el numero maximo de repeticiones sin descanso')
esta5=int(input('¿Cuantas lograste hacer? '))
print('Ahora vas hacer el numero maximo de dominadas supinas subiendo y bajando completamente ')
esta6=int(input('¿Cuantas lograste hacer? '))
print('Ahora vas a ubicarte en plancha de 6 apoyos y haras el tiempo maximo que puedas')
esta7=int(input('¿Cuanto tiempo lograste hacer? en segundos'))
print('Por ultimo mide tu salto verical')
esta8=int(input('¿Cuanto saltas?(Ingresa la medida en cm del salto brutop restale tu estatura)'))
if esta1>= 150:
    pun1=10
elif 100<esta1<150:
    pun1=8
elif 80<esta1<=100:
    pun1=6
elif 40<esta1<=100:
    pun1=4
elif esta1<=40:
    pun1=2
#esta2
if esta2>= 100:
    pun2=10
elif 80<esta2<100:
    pun2=8
elif 60<esta2<=80:
    pun2=6
elif 40<esta2<=60:
    pun2=4
elif esta2<=40:
    pun2=2
#estadistica3
if esta3>= 50:
    pun3=10
elif 40<esta3<50:
    pun3=8
elif 30<esta3<=40:
    pun3=6
elif 20<esta3<=30:
    pun3=4
elif esta3<=20:
    pun3=2
#estadistica4
if esta4>= 50:
    pun4=10
elif 40<esta4<50:
    pun4=8
elif 30<esta4<=40:
    pun4=6
elif 20<esta4<=30:
    pun4=4
elif esta4<=20:
    pun4=2
#estadistica5
if esta5>= 30:
    pun5=10
elif 25<esta5<30:
    pun5=8
elif 20<esta5<=25:
    pun5=6
elif 15<esta5<=20:
    pun5=4
elif esta5<=15:
    pun5=2
#estadistica6
if esta6>= 20:
    pun6=10
elif 15<esta6<20:
    pun6=8
elif 8<esta6<=15:
    pun6=6
elif 3<esta6<=8:
    pun6=4
elif esta6<=3:
    pun6=2
#estadistica7
if esta7>= 180:
    pun7=10
elif 150<esta7<180:
    pun7=8
elif 100<esta7<=150:
    pun7=6
elif 60<esta7<=100:
    pun7=4
elif esta7<=60:
    pun7=2
#estadistica8
if esta8>= 45:
    pun8=10
elif 35<esta8<45:
    pun8=8
elif 25<esta8<=35:
    pun8=6
elif 15<esta8<=25:
    pun8=4
elif esta8<=15:
    pun8=2
#Nivel de juego
PunTF=int(pun1+pun2+pun3+pun4+pun5+pun6+pun7+pun8)