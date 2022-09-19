#Proyecto de convertidor de moneda en python - Jorge Mellizo - 



print("Bienvenidos al convertidor de moneda ")
print("Que moneda quieres convertir")

monedas = ["DOLAR", "EURO", "PESO COLOMBIANO", "PESO ARGENTINO", "YUAN CHINO", "LIBRA ESTERLINA"]

criptomoneda=("BITCOIN, ETHERUM")
print(criptomoneda)
print(monedas)
try:
    moneda=monedas[(monedas.index(input().upper()))] #Error corregido
except:
    print("el valor que pusiste no coincide con los aceptados")
print(moneda)

if moneda == "DOLAR":
    print("Su moneda es: ", moneda)
    monto1=int(input("Que cantidad de dinero que requieres convertir"))
    monedanueva1= monedas[(monedas.index(input("¿A que moneda desea convertir?:")))]
    if monedanueva1 == "EURO":
        monedaconvertida= monto1*1
        print(monto1, "Estos dolares equivalen a:", monedaconvertida, "Euros") #Error corrregido
elif moneda == "EURO":  #Corregir codigo 
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    monto2=int(input())
    input("¿A que moneda desea convertir?:")
    monedanueva2= input()
    if monedanueva2   == "DOLAR":
        monedaconvertida2= monto2*1
        print(monto2, "Estos dolares equivalen a:", monedaconvertida2, "Euros")
elif moneda == "PESO COLOMBIANO":
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    monto3=int(input())
    input("¿A que moneda desea convertir?:")
    monedanueva3= input()
    if monedanueva3   == "EURO":
        monedaconvertida3= monto3*1
        print(monto3, "Estos dolares equivalen a:", monedaconvertida3, "Euros")
elif moneda   == "PESO ARGENTINO":
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    monto4=int(input())
    input("¿A que moneda desea convertir?:")
    monedanueva4= input()
    if monedanueva4   == "EURO":
        monedaconvertida4= monto4*1
        print(monto4, "Estos dolares equivalen a:", monedaconvertida4, "Euros")
elif moneda   == "YUAN CHINO":
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    monto5=int(input())
    input("¿A que moneda desea convertir?:")
    monedanueva5= input()
    if monedanueva5   == "EURO":
        monedaconvertida5= monto5*1
        print(monto5, "Estos dolares equivalen a:", monedaconvertida5, "Euros")
elif moneda   == "LIBRA ESTERLINA":
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    monto6=int(input())
    input("¿A que moneda desea convertir?:")
    monedanueva6= input()
    if monedanueva6   == "EURO":
        monedaconvertida6= monto6*1
        print(monto6, "Estos dolares equivalen a:", monedaconvertida6, "Euros")
elif moneda   == "BITCOIN":
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    montoxxxxxx=int(input())
    input("¿A que moneda desea convertir?:")
    monedanuevaxxxxxx= input()
    if monedanuevaxxxxxx   == "EURO":
        monedaconvertidaxxxxx= montoxxxxxx*1
        print(montoxxxxxx, "Estos dolares equivalen a:", monedaconvertidaxxxxx, "Euros")
elif moneda   == "ETHERUM":
    print("Su moneda es: ", moneda)
    input("Que la cantidad de dinero que requieres convertir")
    montozzz=int(input())
    input("¿A que moneda desea convertir?:")
    monedanuevazzz= input()
    if monedanuevazzz   == "EURO":
        monedaconvertidazzz= montozzz*1
        print(montozzz, "Estos dolares equivalen a:", monedaconvertidazzz, "Euros")
else: 
    print("Digite una moneda existente en y habilitada en el conversor", monedas , criptomoneda, "Estas son las disponibles a conversion")





