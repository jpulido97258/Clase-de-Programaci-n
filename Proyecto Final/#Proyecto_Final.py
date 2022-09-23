#Proyecto_Final//Gestionador de contraseñas con doble verificacion 
import getpass 
ususuario="3steban"#definiciones principales
contraseña="3stebanperezM19781127"
datoverif="cajica"
facebook=("usuario: 3223198808"),("contraseña: 3stebanperezm19781127") #credenciales de apps con el orden, (usuario), (contraseña)
facebookn="facebook"
instagram=facebook#credenciales de apps con el orden, (usuario), (contraseña)
instagramn="instagram"
canva=("DPEREZM75363"),("Lkw@273873738")#credenciales de apps con el orden, (usuario), (contraseña)
canvan="canva"
sap=("usuario: "),("contraseña: ")
listaapps=(facebook , instagram, canva)
for u in range (4):#USUARIO PARA ENTRAR
 username=input("PORFAVOR INGRESE SU USUARIO: ")
 if username==ususuario:
    print("USUARIO CORRECTO")
    break
 else:
    print("SU USUARIO ES INCORRECTO")
for c in range(2):#CONTRASEÑA PARA ENTRAR 
    pasword=getpass.getpass("PORFAVOR INGRESE SU CONTRASEÑA: ")
    if pasword==contraseña:
        print("CONTRASEÑA CORRECTA")
        break
    else:
        print("CONTRASEÑA INCORRECTA")
print("VERIFICACION DE IDENTIDAD")
for v in range(2):#VERIFICACION IDENTIDAD 
    verificacion=input("PORFAVOR INGRESE LUGAR DE EXPEDICION DE TU DOCUMENTO: ")
    if datoverif==verificacion:
        print("BIENVENIDO")
        break
    else:
        print("INCORRECTO")
for a in range(20): #BUSCADOR
    print("INGRESE LA APLICACION EN LA QUE QUIERES BUSCAR TUS CREDENCIALES (EN MINUSCULA Y SIN ESPACIOS)")
    app=input("O SI DESEAS TERMINAR LA BUSQUEDA ESCRIBE FIN: ")
    confirmacion="fin"
    if facebookn==app:
      print(facebook)
    if instagramn==app:
     print(instagram)
    if canvan==app:
     print(canva)
    #if sap==app:
    #if 
    #if 
    if app==confirmacion:
        break  
else:
        print("APLICACION NO REGISTRADA")

"""
Para poder agregrar aplicaciones toca agregar dos variables mas y un if 
"""