#elaborado por Cristina Ronderos Contreras
alfabeto=['l','L','m','M','n','N','ñ','Ñ','g','G','h','H','i','I','w','W','x','X','y','Y','z','Z',' ','a','A','b','B','c','C','d','D','t','T','u','U','v','V','f','F','e','E','j','J','k','K','o','O','p','P','q','Q','r','R','s','S']
frealizar=input('si quiere cifrar un mensaje oprima 1, para descifrar escriba oprima 2 ')
b=1
if int(frealizar)==b:
    tipodec=input('si quiere cifrar palabras oprima 3, para cifrar un codigo numérico oprima 4 ')
    c=3
    #cifrado sencillo a base de la posición de las letras en el alfabeto 
    #creamos una lista del alfabeto para tener como referencia, incluyendo un espacio vacio para facilitar la interpretacion del mensaje en el futuro
    if int(tipodec)==c:
        acifrarl=input('inserte el mensaje a cifrar: ')
        #le pedimos al ususario que inserte el mensaje a cifrar
        acifrarl=list(acifrarl)
        #convertimos la informacion ingresada en una lista
        print(acifrarl)
        for letter in acifrarl:
            cifradol=alfabeto.index(letter)
            #le indicamos al programa que con cada letra insertada busque su posición en el alfabeto, y guarde ese numero en una variable
            print(cifradol, end=' ')
            #mostramos en pantalla el mensaje cifrado, sin salto de linea(logrado gracias a end=' ')
    else:
        acifrarn=input('inserte el codigo a cifrar').split()
        acifrarn=list(acifrarn)
        print(acifrarn)
        for number in acifrarn:
            cifradon=alfabeto[int(number)]
            print(cifradon, end=' ')
#elaborado por Cristina Ronderos Contreras
else:
    tipoded=input('si quiere descifrar palabras oprima 3, para descifrar un codigo numérico oprima 4')
    c=3
    if int(tipoded)==c:
        #tenemos como referencia la misma lista del alfabeto que se usa a la hora de codificar
        descifrarl=input('inserte a continuación el mensaje a revelar: ').split()
        #le pedimos al usuario que inserte los numeros que revelaran el mensaje, y los mantenemos separados como los ingreso el usuario con.split()
        for number in descifrarl:
            #si el numero se encuentra entre los insertados por el usuario entonces
            descifradol=alfabeto[int(number)]
            #definimos que el mensaje descifrado es igual a la letra en la posición de ese numero en el alfabeto(despues de convertir el numeor a entero)
            print(descifradol, end=' ')
            #mostramos el mensaje descifrado en pantalla sin saltos gracias a =end' '
    else:
        descifrarn=input('inserte el codigo a revelar: ')
        for letter in descifrarn:
            descifradon=alfabeto.index(letter)
            print(descifradon, end=' ')
            #elaborado por Cristina Ronderos Contreras
