# Vamos a ver como puedes cambiar tu forma fisica
print("Vamos a ver cuantas calorias debes consumir para mantenerse")
print ("Colocar si es hombre o mujer")
genero = input("Por favor especifica tu género escribiendo la palabra 'Hombre' o 'Mujer': ")
a= ("Mujer")
b= ("Hombre")
if a == genero:
    print("Que tan sedentario eres", "\n1,2 para personas sedentarias",
    "\n1,375 para personas con poca actividad física (ejercicio de 1 a 3 veces por semana)",
    "\n1,55 para individuos que realizan actividad moderada (ejercicio de 3 a 5 veces por semana)", 
    "\n1,725 para personas que hacen actividad intensa (ejercicio de 6 a 7 veces por semana)", 
    "\n1,9 para atletas profesionales (entrenamientos de más de 4 horas diarias): ")
    sedentario=float(input ("Coloca el numero que concideras de sedentarismo, este numero se encuentra antes de cada texto explicativo de arriba ej:1.2: "))
    print("vamos a realizar el siguiente calculo ", a) # mujer
    peso =float(input("Cuanto pesas?: "))
    estatura= float(input("Cuanto mides?, coloca tu estatura en centimetro ej: 150 : "))
    edadmujer= int(input("Coloca tu edad mujer: "))
    rta1 = float(9.6*peso)
    rta2 = float (655 + rta1)
    rta22 = float(1.8*estatura)
    rta3 = float(4.7*edadmujer)
    rta4 = float (rta2+rta22-rta3)
    rtafinalm =float(rta4 * sedentario)
    print("usted necesesita: " ,rtafinalm, "calorias para mantener su peso")
    print("Que quiere hacer con su cuerpo")
    print("Quiere aumentar de peso o bajar?")
    Respuesta = input("'Subir' - 'Bajar': ")
    Sm= ("Subir")
    Bm= ("Bajar")
    peso3 = int(input("coloca tu peso deseado: "))
    subir = float()
    rtt2 = float()
    rtt4= float()
    if Sm == Respuesta:
        while peso3 < peso:
            print("el peso ingresado es incorrecto, usted dijo que pesaba ", peso, " y el peso " , peso3, " deseado es menor, por favor escriba el peso deseado mayor al inicial")
            peso3 = int(input("coloca tu peso deseado: "))
        else: rtt2 == Sm
        print(rtafinalm + 120 )
        print("Necesita consumir mas calorias por dia aumente 120")
        print("Estas son las calorias semanales para llegar: " ,peso3 )
        print(rtafinalm + 120 * 7 )
        if Bm == Respuesta: 
            while peso3 > peso:
                print("el peso ingresado es incorrecto, usted dijo que pesaba ", peso, " y el peso " , peso3, " deseado es mayor, por favor escriba el peso deseado menor al inicial")
                peso3 = int(input("Coloca tu peso deseado"))
            else: rtt4 == Bm
            print(rtafinalm - 120 )
            print("Necesita consumir menos calorias por dia disminuya 120")
            print("Estas son las calorias semanales para llegar: " ,peso3 )
            print(rtafinalm - 120 * 7 )

if b == genero:
    print("Que tan sedentario eres","\n1,2 para personas sedentarias \n1,375 para personas con poca actividad física (ejercicio de 1 a 3 veces por semana) \n1,55 para individuos que realizan actividad moderada (ejercicio de 3 a 5 veces por semana).\n1,725 para personas que hacen actividad intensa (ejercicio de 6 a 7 veces por semana).\n1,9 para atletas profesionales (entrenamientos de más de 4 horas diarias).")
    sedentario2= float(input ("Coloca el numero que concideras de sedentarismo, este numero se encuentra antes de cada texto explicativo de arriba ej:1.2: "))
    print("Vamos a realizar el siguiente calculo ", b) #hombre
    peso2 = int(input("coloca tu peso: "))
    print("Aca vamos a evidenciar cuanto necesitas para mantener a tu cuerpo:")
    print("Coloca tu estatura en centímetros Ej: 180 ")
    estatura2 = int(input())
    edadhombre = int(input("coloca tu edad hombre: "))
    rta1 = float(13.752*peso2)
    rta2 = float (66 + rta1)
    rta22 = float(5*estatura2)
    rta3 = float(6.755*edadhombre)
    rta4 = float (rta2+rta22-rta3)
    rtafinal2 = float(rta4 * sedentario2)
    print("usted necesesita: " ,  rtafinal2, "calorias para mantener su peso")
    print("Que quiere hacer con su cuerpo")
    print("Quiere aumentar de peso o bajar?")
    Respuesta = input("'Subir' - 'Bajar': ")
    S= ("Subir")
    B= ("Bajar")
    aumentar =float
    rtt=float()
    rtt3=float()
    peso3 = int(input("coloca tu peso deseado: "))
    if S == Respuesta:
            while peso3 < peso2:
                print("el peso ingresado es incorrecto, usted dijo que pesaba ", peso2, " y el peso " , peso3, " deseado es menor, por favor escriba el peso deseado mayor al inicial")
                peso3 = int(input("coloca tu peso deseado: "))
    
            print("Necesita consumir mas calorias por dia aumente 120")
            print(rtafinal2 + 120 )
            print("Estas son las calorias semanales para llegar: " ,peso3 )
            print(rtafinal2 + 120 * 7 )
    if B == Respuesta:
        while peso3 > peso2:
            print("el peso ingresado es incorrecto, usted dijo que pesaba ", peso2, " y el peso " , peso3, " deseado es mayor, por favor escriba el peso deseado menor al inicial")
            peso3 = int(input("Coloca tu peso deseado"))

        print(rtafinal2 - 120 )
        print("Necesita consumir menos calorias por dia disminuya 120")
        print("Estas son las calorias semanales para llegar: " ,peso3 )
        print((rtafinal2 - 120) * 7 )

#Lista de alimentos.
print("Estos los alimentos mas pedidos de la universidad")
print("Pan de bono, Jugo de naranja , Waffles fruta helado, Pastel de champiñon , Porción de fruta")
print("Estos alimentos añadirian este numero de calorias ")

print("Estos son los alimentos de la universidad")
print ("puedes ayudarte con estos para determinar tu objetivo")

print("Mas caloricos")
Caloricos = float() 
pasteleria = {"Arepa con queso":280,"cheesecake" : 321,"Churro": 361, "Delicia de limon o milo": 196,"empanada chilena": 335, "Milhoja":448, "Pastel de pollo": 311} 
for k, v in pasteleria.items():
    print('k=', k, ', v=', v)
    
Helados  = {"Torta individual de frutos del bosque":200,"Vaso de chocoloate" : 216,"Vaso frutos del bosque": 196, "Vaso de milky way": 225,"Torta de oreo": 249}
for k, v in pasteleria.items():
    print('k=', k, ', v=', v)

snacks= {"Achiras Ramo":90,"Barquillo Piazza":140,"Chocmelos Mickey Mouse":110,"Chocolate Burbuja Jet":70,"Chocolatina con Mani Jumbo":110,"Chocolatina Gol":160,"Chocolatina Jet":200,"Chocolatina Snickers":250,"Galletas Festival":220,"Galletas Fusion de Cereales Tosh":120,"Galletas Miel Tosh":120,"Galletas Quimbaya":140,"Galletas Wafer Jet":50,"Ponque Barra de Chocorramo":170,"Ponque Chocorramo":160,"Uvas Cheveres":28}
for k,v in snacks.items():
    print('k=',k, ',v=',v)

Frutas = {"Arándanos":57,"Manzana" : 52,"Mango": 60 , "Moras": 43 ,"Plátano / Banana": 89 }
for k, v in pasteleria.items():
    print('k=', k, ', v=', v)
Calorias = int 
print ("Colocar si quieres calorias, escribe Caloricos, si quieres bajas calorias escribe Poco calorico: ")
C= ("Caloricos")
P = ("Poco caloricos")
if C == Calorias:
    print (pasteleria, Helados)
if P == Calorias:
    print (Frutas, snacks)
print ("Mediante esto puedes mirar que alimentos te ayudaran en tu proseso")


