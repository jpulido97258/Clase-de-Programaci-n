#Proyecto de convertidor de moneda en python - Jorge Mellizo - 

import urllib.request      #CODE BITCOIN
import json

print("Bienvenidos al convertido de moneda ")
print("¿Que moneda desea convertir?")


monedas = ["DOLAR", "EURO", "PESO COLOMBIANO", "PESO ARGENTINO", "YUAN CHINO", "LIBRA ESTERLINA","BITCOIN"]

print(monedas)
try:
    moneda=monedas[(monedas.index(input().upper()))] #Error corregido
except:
    print("el valor que pusiste no coincide con los aceptados")
print(moneda)

if moneda == "DOLAR":      #DOLAR
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "EURO":
        monedaconvertida= monto1*1
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1) #Error corrregido
    elif monedanueva1 == "PESO COLOMBIANO":
        monedaconvertida= monto1*4431
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO ARGENTINO":
        monedaconvertida= monto1*144.8
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "YUAN CHINO":
        monedaconvertida= monto1*7.03
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "LIBRA ESTERLINA":
        monedaconvertida= monto1*0.088
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)      
    else:
        print("Digite una moneda existente en y habilitada en el conversor", monedas ,  "Estas son las disponibles a conversion") #FIN DOLAR
elif moneda == "EURO":      #EURO
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "DOLAR":
        monedaconvertida= monto1*1
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO COLOMBIANO":
        monedaconvertida= monto1*4431
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO ARGENTINO":
        monedaconvertida= monto1*144.8
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "YUAN CHINO":
        monedaconvertida= monto1*7.03
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "LIBRA ESTERLINA":
        monedaconvertida= monto1*0.088
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    else:
        print("Digite una moneda existente en y habilitada en el conversor", monedas,  "Estas son las disponibles a conversion") #FIN EURO
elif moneda == "PESO COLOMBIANO":    #PESO COLOMBIANO
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "DOLAR":
        monedaconvertida= monto1*0.00023
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "EURO":
        monedaconvertida= monto1*0.00023
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO ARGENTINO":
        monedaconvertida= monto1*0.033
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "YUAN CHINO":
        monedaconvertida= monto1*0.0016
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "LIBRA ESTERLINA":
        monedaconvertida= monto1*0.00020
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    else:
        print("Digite una moneda existente en y habilitada en el conversor", monedas,  "Estas son las disponibles a conversion") #FIN PESO COLOMBIANO
elif moneda == "PESO ARGENTINO":    #PESO ARGENTINO
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "DOLAR":
        monedaconvertida= monto1*0.0069
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "EURO":
        monedaconvertida= monto1*0.0069
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO COLOMBIANO":
        monedaconvertida= monto1*30.53
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "YUAN CHINO":
        monedaconvertida= monto1*0.049
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "LIBRA ESTERLINA":
        monedaconvertida= monto1*0.0061
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    else:
        print("Digite una moneda existente en y habilitada en el conversor", monedas ,"Estas son las disponibles a conversion") #FIN PESO ARGENTINO
elif moneda == "YUAN CHINO":      #YUAN CHINO
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "DOLAR":
        monedaconvertida= monto1*0.14
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "EURO":
        monedaconvertida= monto1*0.14
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO ARGENTINO":
        monedaconvertida= monto1*20.60
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO COLOMBIANO":
        monedaconvertida= monto1*628.92
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "LIBRA ESTERLINA":
        monedaconvertida= monto1*0.12
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    else:
        print("Digite una moneda existente en y habilitada en el conversor", monedas, "Estas son las disponibles a conversion") #FIN YUAN CHINO
elif moneda == "LIBRA ESTERLINA":   #LIBRA ESTERLINA
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "DOLAR":
        monedaconvertida= monto1*1.14
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "EURO":
        monedaconvertida= monto1*0.14
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO ARGENTINO":
        monedaconvertida= monto1*165.05
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "YUAN CHINO":
        monedaconvertida= monto1*8.01
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    elif monedanueva1 == "PESO COLOMBIANO":
        monedaconvertida= monto1*5038.08
        print(monto1, "Estos" ,moneda, "equivalen a:", monedaconvertida, monedanueva1)
    else:
        print("Digite una moneda existente en y habilitada en el conversor", monedas, "Estas son las disponibles a conversion") #FIN LIBRA ESTERLINA
elif moneda == "BITCOIN":      #BITCOIN-DOLAR
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir: "))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:").upper()))]
    if monedanueva1 == "DOLAR":
        data = urllib.request.urlopen("http://api.bitcoincharts.com/v1/weighted_prices.json")
        def convert_to_bitcoin(amount, currency):
            bitcoins = json.loads(data.read())
            A = float(bitcoins[currency]["24h"]) * amount
            print(monto1, "Estos" ,moneda, "equivalen a:", A , monedanueva1)
        convert_to_bitcoin(monto1, "USD")
    elif monedanueva1 == "EURO":
        data = urllib.request.urlopen("http://api.bitcoincharts.com/v1/weighted_prices.json")
        def convert_to_bitcoin(amount, currency):
            bitcoins = json.loads(data.read())
            A = float(bitcoins[currency]["24h"]) * amount
            print(monto1, "Estos" ,moneda, "equivalen a:", A , monedanueva1)
        convert_to_bitcoin(monto1, "USD")
    else:
        print("Elija bien jajaa")
else: 
    print("Digite una moneda existente en y habilitada en el conversor", monedas, "Estas son las disponibles a conversion")

print("Fin Ejecución")