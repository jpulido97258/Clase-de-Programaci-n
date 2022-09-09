#usuario y contraeña
edward20=str
usuario = [edward20]
contraseña = [12345]

contador = 0
loged = False #Esto con ayuda de un compañero :)
us=str
pas=str

print("C");

while loged == False and contador != 3: 
        for e in usuario:
            us = input("Escribre tu nombre de usuario: ")
            if usuario == us:
                print("El usuario es correcto.")
                break
            else:
                print("El usuario es incorrecto")
            contador = contador +1
            if contador == 3: 
                print("Numero de intentos maximos, Reinicia el programa")
                break
        
        if usuario == us:
            for e in contraseña:
                pas = input("Escribe tu contraseña:")
                if pas == contraseña:
                    print("Contraseña correcta")
                    print("Sesion iniciada")
                    loged = True 
                    break
                print("Contraseña incorrecta")
                intentos = intentos +1
                if contador == 3: 
                    print("Numero de intentos maximos, Reinicia el programa")
                break
