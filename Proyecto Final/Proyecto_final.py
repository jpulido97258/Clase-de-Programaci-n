#Codigo Trabajo Final
#Este proyecto se llamara MIRENDI
#Primero ingresar DAtos generales
#import numpy 
print('Bienvenido a nuestro sistema')
print('Por favor ingresa tus datos para empezar')
print('¿Eres Hombre o Mujer?')
genero=str(input())
print('Ingresa tu edad')
edad= int(input())
print('Digita en cm cuanto mides')
altura=int(input())
print('¿Cual es tu peso en kg? el verdadero xd' )
peso=float(input())
#Seleccionar que proceso quiere realizar
print('¿Que quieres realizar el dia de hoy:')
print('Digita 1 para realizar una evaluacion general')
print('Digita 2 para realizar una evaluacion especifica')
proceso=int(input())
if proceso==1:
    #entradas
    print('Realizaremos el proceso general')
    print('Comencemos') 
    print('Vamos a iniciar con tus estadísticas de recepción, vas a necesitar la ayuda de un compañero y un Hula Hula, tu compañero se ubicara en la posición 4 de la cancha y ubica el hula hula en la posición dos.' )
    print('Tu compañero te lanzara 10 balones fáciles(Que vayan dirigidos a ti) esos balones los recibirás y contaras cuantos entran dentro del hula hula.' )
    print('¿Cuántos balones cayeron dentro del aro?' )
    balin1=float(input())
    print('Listo vamos por la segunda prueba' )
    print('Vas a repetir el ejercicio anterior, pero ahora tu compañero te debe rematar los balones en tu dirección' )
    print('¿Cuántos balones cayeron dentro del aro?' )
    balin2=float(input())
    print('Listo vamos por la tercera prueba' )
    print('Ahora los balones que tire tu compañero serán balones de rescate( Balones no dirigidos a ti) donde debes llegar a esos balones y contar cuantos caen dentro del aro')
    print('¿Cuántos balones cayeron dentro del aro?' )
    balin3=float(input())
    pro1=float(balin1*0.2)
    pro2=float(balin2*0.3)
    pro3=float(balin3*0.5)
    resR1=int((pro1+pro2+pro3))#ESte es el porcentaje de eficiencia
    resR2=int(((balin1+balin2+balin3)*100)/30)#este es el porcentaje de precision
    #VOLEO
    print('Comencemos con las pruebas de voleo')
    print('Para esta prueba vas a necesitar un compañero y un balón' )
    print('Para la primera parte te vas a ubicar en 2 y  vas a pedir que te pasen el balón fácilmente para que en forma de voleo mandes el balón a posición 4 (El balón debe pasar a 50cm de la antena y debe ir en forma de parábola) lanzaras 15 balones y contaras cuantos pasaron por el punto de destino en una buena forma ( sin hacer doble golpe o levantamiento de balón)' )
    print('¿Cuántos balones pasaron por la zona determinada?' )
    balV1=int(input())
    print('Ahora repetirás los lanzamientos de la misma manera pero ahora que el balón pase por la mitad de la malla a 30 cm de ella' )
    balV2=int(input('¿Cuántos balones pasaron por la zona determinada? '))
    print('La siguiente prueba será pasar los balones a posición 2 donde el balón debe pasar a 50 cm de la antena derecha de la malla y a 50 cm de la malla' )
    balV3=int(input('¿Cuántos balones pasaron por la zona determinada? '))
    #print('La siguiente prueba será pasar los balones a posición 4 donde el balón debe pasar a 50 cm de la antena derecha de la malla y a 50 cm de la malla') 
    print('Ahora vas a pedir que te lancen los balones altos a un lugar diferente, los balones deben ser difíciles de pasar, vas a levantar 5 balones a 4, 5 balones a 3 y 5 balones a 2, cada uno en sus zonas determinadas anteriormente.' )
    balV4=int(input('¿Cuántos balones pasaron por las zonas determinadas?'))
    pro4=float(balV1*0.2)
    pro5=float(balV2*0.2)
    pro6=float(balV3*0.2)
    pro7=float(balV4*0.4)
    EfectividadVoleo=int(((pro4+pro5+pro6+pro7)*10)/15)
    PresicionVoleo=int(((balV1+balV2+balV3+balV4)*100)/60)
    #SERVICIO
    print('Comencemos con tu evaluación de servicio')
    print('Vamos a realizar 3 tipos de saques : servicio seguro, servicio alto y servicio con salto')
    print('Vas a necesitar un aro y un balon')
    print('Ubica el aro en zona 1 del campo contrario y realiza 5 servicios seguros,  5 servicios altos y 5 servicios con saltos, todos dirogidos al aro')
    BalSin1= int(input('¿Cuántos servicios seguros cayeron a dentro del aro? '))
    BalSin2= int(input('¿Cuántos servicios altos cayeron a dentro del aro? '))
    BalSin3= int(input('¿Cuántos servicios con salto cayeron a dentro del aro? '))
    print('Vamos a repetir el proceso pero ubicando el aro en zona 6 del campo contrario.')
    BalSin4= int(input('¿Cuántos servicios seguros cayeron a dentro del aro? '))
    BalSin5= int(input('¿Cuántos servicios altos cayeron a dentro del aro? '))
    BalSin6= int(input('¿Cuántos servicios con salto cayeron a dentro del aro? '))
    print('Por último vamos a repetir el proceso pero ubicando el aro en zona 5 del campo contrario.')
    BalSin7= int(input('¿Cuántos servicios seguros cayeron a dentro del aro? '))
    BalSin8= int(input('¿Cuántos servicios altos cayeron a dentro del aro? '))
    BalSin9= int(input('¿Cuántos servicios con salto cayeron a dentro del aro? '))
    Dat1=float((BalSin1+BalSin2+BalSin3)*0.25)
    Dat2=float((BalSin4+BalSin5+BalSin6)*0.25)
    Dat3=float((BalSin7+BalSin8+BalSin9)*0.5)
    PresicionServicio=int(((BalSin1+BalSin2+BalSin3+BalSin4+BalSin5+BalSin6+BalSin7+BalSin8+BalSin9)*100)/45)
    EfectividadServicio=int(((Dat1+Dat2+Dat3)*10)/15)
    #REMATE
    print('Comencemos con el proceso de remate')
    print('Vas a necesitar la ayuda de un compañero que te levante el balon y un aro')
    print('Vas a colocar el aro en zona 1 del campo contrario y vas a realizar a rematar 3 balones dirigidos  al aro, 3 remates por punta, 3 remates por centro y 3 remates por opuesto')

    BalRin11=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta? '))
    BalRin12=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
    BalRin13=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
    BalRin1=int(BalRin11+BalRin12+BalRin13)

    print('Ahora coloca el aro en zona 6 del campo contrario, repite el número de remates')

    BalRin21=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta? '))
    BalRin22=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
    BalRin23=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
    BalRin2=int(BalRin21+BalRin22+BalRin23)

    print('Ahora coloca el aro en zona 5 del campo contrario, repite el número de remates')

    BalRin31=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta? '))
    BalRin32=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
    BalRin33=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
    BalRin3=int(BalRin31+BalRin32+BalRin33)
    Prescicion1=float(BalRin1*0.4)
    Prescicion2=float(BalRin2*0.3)
    Prescicion3=float(BalRin3*0.3)
    PresicionRemate=int(((BalRin11+BalRin12+BalRin13+BalRin21+BalRin22+BalRin23+BalRin31+BalRin32+BalRin33)*100)/27)
    EfectividadRemate=int(((Prescicion1+Prescicion2+Prescicion3)*10)/9)
    #EVALUACIONFUERZA
    print('Vamos a medir que tal estan tus niveles de deztraza fisica')
    print('Vas a medir la fuerza de tus brazos, piernas, abdomen y esaplda, ademas de velocidad y Hagilidad')
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
    print('Ahora vas a hacer dorsales, haz el numero maximo de repeticiones sin descanso')
    esta5=int(input('¿Cuantas lograste hacer? '))
    print('Ahora vas hacer el numero maximo de dominadas supinas subiendo y bajando completamente ')
    esta6=int(input('¿Cuantas lograste hacer? '))
    print('Ahora vas a ubicarte en plancha de 6 apoyos y haras el tiempo maximo que puedas')
    esta7=int(input('¿Cuanto tiempo lograste hacer? en segundos '))
    print('Por ultimo mide tu salto verical')
    esta8=int(input('¿Cuanto saltas?(Ingresa la medida en cm del salto bruto restale tu estatura) '))
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
    #CAJA NEGRA
    Eficienciageneral=int((resR1+EfectividadVoleo+EfectividadRemate+EfectividadServicio)/4)
    Presiciongeneral=int((resR2+PresicionRemate+PresicionServicio+PresicionVoleo)/4)
    level=int(Eficienciageneral+Presiciongeneral)
    if level>=125:
        nivelE=str('Profesional')
    elif 125>level>=95:
        nivelE=str('Avanzado')
    elif 95>level>=75:
        nivelE=str('Alto')
    elif 75>level>=50:
        nivelE=str('Promedio')
    elif 50>level>=0:
        nivelE=str('Bajo')
    if PunTF >=70:
        EstadoF=str('Estas en buena forma')
    elif 50<PunTF<=70:
        EstadoF=str('Estas bien pero debes mejorar')
    elif 30<PunTF<=50:
        EstadoF=str('Debes mejorar tu estado fisico')
    elif PunTF<=30:
        EstadoF=str('¡COMIENZA HACER EJERCICIO!')
    listaresaultados=[EfectividadRemate, EfectividadServicio, EfectividadVoleo, resR1]
    posicionideal=max(listaresaultados)
    if posicionideal==EfectividadRemate:
        psid=str('Atacante centro')
    elif posicionideal==EfectividadServicio:
        psid=str('Opuesto')
    elif posicionideal==EfectividadVoleo:
        psid=str('Pasador')
    elif posicionideal==resR1:
        psid=str('Libero')
    if altura>=190:
        psid2=str('Centro')
    elif 190>altura>=180:
        psid2=str('Atacante auxiliar')
    elif 180>altura>=170:
        psid2=str('Opuesto')
    elif altura<170:
        psid2=str('Libero')
    #SALIDAS
    print('Segun tus resultados tu nivel de juego es : ', nivelE)
    print('Tus niveles de eficiencia son(Cada numero es evaluado sobre 10, por ejemplo si tu numero es 7 significa que de cada 10 balones 7 sera la eficiencia):')
    print('Eficiencia Recepcion: ',resR1)
    print('Eficiencia Saque: ', EfectividadServicio)
    print('Eficiencia Remate: ', EfectividadRemate)
    print('Eficiencia del Voleo: ', EfectividadVoleo)
    print('Tus niveles de presicion especifico son:')
    print('Presicion Recepcion: ',resR2, '%')
    print('Presicion Saque: ', PresicionServicio, '%')
    print('Presicion Remate: ', PresicionRemate, '%')
    print('Presicion del Voleo: ', PresicionVoleo, '%')
    print('Tu recomendacion en estado fisico es: ', EstadoF)
    print('Tu posicion ideal por rendimiento es: ', psid)
    print('Tu posicion ideal por tus cualidades fisicas es: ', psid2)
elif proceso==2:
    seleccion=(int(input('Elige que quieres hacer: (1) para evaluacion de remate, (2) para evaluacion de voleo, (3) para evaluacion de recepcion, (a) para evaluacion de servicio y (5) para evaluacion de fuerza: ')))
    if seleccion==1:
        print('Comencemos con el proceso de remate')
        print('Vas a necesitar la ayuda de un compañero que te levante el balon y un aro')
        print('Vas a colocar el aro en zona 1 del campo contrario y vas a realizar a rematar 3 balones dirigidos  al aro, 3 remates por punta, 3 remates por centro y 3 remates por opuesto')

        BalRin11=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta? '))
        BalRin12=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
        BalRin13=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
        BalRin1=int(BalRin11+BalRin12+BalRin13)

        print('Ahora coloca el aro en zona 6 del campo contrario, repite el número de remates')

        BalRin21=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta? '))
        BalRin22=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
        BalRin23=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
        BalRin2=int(BalRin21+BalRin22+BalRin23)

        print('Ahora coloca el aro en zona 5 del campo contrario, repite el número de remates')

        BalRin31=int(input('¿Cuántos balones cayeron dentro del aro, cuando atacabas por punta? '))
        BalRin32=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por centro? '))
        BalRin33=int(input('¿Cuántos balones cayeron dentro del aro,cuando atacabas por opuesto? '))
        BalRin3=int(BalRin31+BalRin32+BalRin33)
        Prescicion1=float(BalRin1*0.4)
        Prescicion2=float(BalRin2*0.3)
        Prescicion3=float(BalRin3*0.3)
        PresicionRemate=int(((BalRin11+BalRin12+BalRin13+BalRin21+BalRin22+BalRin23+BalRin31+BalRin32+BalRin33)*100)/27)
        EfectividadRemate=int(((Prescicion1+Prescicion2+Prescicion3)*10)/9)
        print('Tu efectividad de remate es: ',EfectividadRemate, ' y la presicion de tu remate es: ', PresicionRemate, '%')
    elif seleccion==2:
        print('Comencemos con las pruebas de voleo')
        print('Para esta prueba vas a necesitar un compañero y un balón' )
        print('Para la primera parte te vas a ubicar en 2 y  vas a pedir que te pasen el balón fácilmente para que en forma de voleo mandes el balón a posición 4 (El balón debe pasar a 50cm de la antena y debe ir en forma de parábola) lanzaras 15 balones y contaras cuantos pasaron por el punto de destino en una buena forma ( sin hacer doble golpe o levantamiento de balón)' )
        print('¿Cuántos balones pasaron por la zona determinada?' )
        balV1=int(input())
        print('Ahora repetirás los lanzamientos de la misma manera pero ahora que el balón pase por la mitad de la malla a 30 cm de ella' )
        balV2=int(input('¿Cuántos balones pasaron por la zona determinada? '))
        print('La siguiente prueba será pasar los balones a posición 4 donde el balón debe pasar a 50 cm de la antena derecha de la malla y a 50 cm de la malla' )
        balV3=int(input('¿Cuántos balones pasaron por la zona determinada? '))
        #print('La siguiente prueba será pasar los balones a posición 4 donde el balón debe pasar a 50 cm de la antena derecha de la malla y a 50 cm de la malla') 
        print('Ahora vas a pedir que te lancen los balones altos a un lugar diferente, los balones deben ser difíciles de pasar, vas a levantar 5 balones a 4, 5 balones a 3 y 5 balones a 2, cada uno en sus zonas determinadas anteriormente.' )
        balV4=int(input('¿Cuántos balones pasaron por las zonas determinadas?'))
        pro4=float(balV1*0.2)
        pro5=float(balV2*0.2)
        pro6=float(balV3*0.2)
        pro7=float(balV4*0.4)
        EfectividadVoleo=int(((pro4+pro5+pro6+pro7)*10)/15)
        PresicionVoleo=int(((balV1+balV2+balV3+balV4)*100)/60)
        print('La efecitividad de tu voleo es: ', EfectividadVoleo)
        print('La presicion de tu voleo es: ', PresicionVoleo, '%')
    elif seleccion==3:
        print('Comencemos') 
        print('Vamos a iniciar con tus estadísticas de recepción, vas a necesitar la ayuda de un compañero y un Hula Hula, tu compañero se ubicara en la posición 4 de la cancha y ubica el hula hula en la posición dos.' )
        print('Tu compañero te lanzara 10 balones fáciles(Que vayan dirigidos a ti) esos balones los recibirás y contaras cuantos entran dentro del hula hula.' )
        print('¿Cuántos balones cayeron dentro del aro?' )
        balin1=float(input())
        print('Listo vamos por la segunda prueba' )
        print('Vas a repetir el ejercicio anterior, pero ahora tu compañero te debe rematar los balones en tu dirección' )
        print('¿Cuántos balones cayeron dentro del aro?' )
        balin2=float(input())
        print('Listo vamos por la tercera prueba' )
        print('Ahora los balones que tire tu compañero serán balones de rescate( Balones no dirigidos a ti) donde debes llegar a esos balones y contar cuantos caen dentro del aro')
        print('¿Cuántos balones cayeron dentro del aro?' )
        balin3=float(input())
        pro1=float(balin1*0.2)
        pro2=float(balin2*0.3)
        pro3=float(balin3*0.5)
        resR1=int(pro1+pro2+pro3)#ESte es el porcentaje de eficiencia
        resR2=int(((balin1+balin2+balin3)*100)/30)#este es el porcentaje de precision
        print('la eficencia de tu recepcion es: ',resR1, 'y el porcentaje de tu recepcion es: ',resR2, '%')
    elif seleccion==4:
        print('Comencemos con tu evaluación de servicio')
        print('Vamos a realizar 3 tipos de saques : servicio seguro, servicio alto y servicio con salto')
        print('Vas a necesitar un aro y un balon')
        print('Ubica el aro en zona 1 del campo contrario y realiza 5 servicios seguros,  5 servicios altos y 5 servicios con saltos, todos dirogidos al aro')
        BalSin1= int(input('¿Cuántos servicios seguros cayeron a dentro del aro? '))
        BalSin2= int(input('¿Cuántos servicios altos cayeron a dentro del aro? '))
        BalSin3= int(input('¿Cuántos servicios con salto cayeron a dentro del aro? '))
        print('Vamos a repetir el proceso pero ubicando el aro en zona 6 del campo contrario.')
        BalSin4= int(input('¿Cuántos servicios seguros cayeron a dentro del aro? '))
        BalSin5= int(input('¿Cuántos servicios altos cayeron a dentro del aro? '))
        BalSin6= int(input('¿Cuántos servicios con salto cayeron a dentro del aro? '))
        print('Por último vamos a repetir el proceso pero ubicando el aro en zona 5 del campo contrario.')
        BalSin7= int(input('¿Cuántos servicios seguros cayeron a dentro del aro? '))
        BalSin8= int(input('¿Cuántos servicios altos cayeron a dentro del aro? '))
        BalSin9= int(input('¿Cuántos servicios con salto cayeron a dentro del aro? '))
        Dat1=float((BalSin1+BalSin2+BalSin3)*0.25)
        Dat2=float((BalSin4+BalSin5+BalSin6)*0.25)
        Dat3=float((BalSin7+BalSin8+BalSin9)*0.5)
        PresicionServicio=int(((BalSin1+BalSin2+BalSin3+BalSin4+BalSin5+BalSin6+BalSin7+BalSin8+BalSin9)*100)/45)
        EfectividadServicio=int(((Dat1+Dat2+Dat3)*10)/15)
        print('La efecitividad de tu servicio es: ', EfectividadServicio)
        print('La presicion de tu servicio es: ', PresicionServicio, '%')
    elif seleccion==5:
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
        print('Ahora vas a hacer dorsales, haz el numero maximo de repeticiones sin descanso')
        esta5=int(input('¿Cuantas lograste hacer? '))
        print('Ahora vas hacer el numero maximo de dominadas supinas subiendo y bajando completamente ')
        esta6=int(input('¿Cuantas lograste hacer? '))
        print('Ahora vas a ubicarte en plancha de 6 apoyos y haras el tiempo maximo que puedas')
        esta7=int(input('¿Cuanto tiempo (en segundos) lograste hacer? '))
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
        PunTF=int(pun1+pun2+pun3+pun4+pun5+pun6+pun7+pun8)
        if PunTF >=70:
            EstadoF=str('Estas en buena forma')
        elif 50<PunTF<=70:
            EstadoF=str('Estas bien pero debes mejorar')
        elif 30<PunTF<=50:
            EstadoF=str('Debes mejorar tu estado fisico')
        elif PunTF<=30:
            EstadoF=str('¡COMIENZA HACER EJERCICIO!')
        print(EstadoF)


print('Fin del programa')
print('Gracias por preferirnos')